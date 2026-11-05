"""Static website checks: internal links, release metadata and safe public files."""
from html.parser import HTMLParser
from pathlib import Path
import json
from urllib.parse import urlsplit,unquote

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=set();self.links=[];self.linksById={};self.headings=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids,'Duplicate anchor'
            self.ids.add(attrs['id'])
        if tag=='a':
            self.links.append(attrs.get('href',''))
            if 'id' in attrs:self.linksById[attrs['id']]=attrs.get('href','')
        if tag in ('h1','h2','h3'):self.headings.append(tag)
        assert tag not in ('script','iframe') or not attrs.get('src','').startswith('http'),'No third-party resource at page load'
pages={p.name:Page(p.read_text(encoding='utf-8')) for p in ROOT.glob('*.html')}
for name,page in pages.items():
    assert page.headings.count('h1')==1,name
    for href in page.links:
        url=urlsplit(href)
        if url.scheme or url.netloc:continue
        target=unquote(url.path) or name
        assert (ROOT/target).is_file(),(name,href)
        if url.fragment:assert url.fragment in pages[target].ids,(name,href)
release=json.loads((ROOT/'release.json').read_text())
assert release['version']=='0.2.0-beta.2-trim-pointers'
assert release['channel']=='public beta'
assert release['binaryChangesFromPromotedBuild'] is True
assert release['windows']['version']=='0.3.0-beta.1'
assert release['windows']['pluginName']=='XPPanelsQuestBridge'
assert release['windows']['desktopIcon']['sha256']=='20972858356a3220b9bf5c52d506915ceda64cdc3686142c9296f19df4927333'
assert release['windows']['nativeSectionsUnchanged'] is True
assert release['windows']['pluginBundled'] is True
assert release['windows']['highQualityVideoAdded'] is False
assert release['windows']['requiresQuestRebuild'] is False
assert release['windows']['capturePESectionsMatchPreviousRelease'] is True
assert release['windows']['compatibleQuest']=={key:release['metaBeta'][key] for key in ('version','versionCode','sha256')}
assert pages['index.html'].linksById['windows-download']==release['windows']['downloadUrl']
assert pages['index.html'].linksById['mac-download']==release['mac']['downloadUrl']
assert release['windows']['signing']=='Self-signed; not automatically trusted by Windows'
assert release['mac']['architecture']=='arm64'
assert release['mac']['sha256']=='13bca320ea205987c8a7cc3373f8d5e2f8def5d8b054d5b890c5709fca14ec2a'
assert release['mac']['notarization']=='Accepted and stapled'
assert release['metaBeta']['invite']=='https://www.meta.com/s/4YJ4Mw9Hd'
assert release['metaBeta']['debuggable'] is False
assert release['metaBeta']['buildId']=='1486185411233879'
assert release['metaBeta']['versionCode']==20002
assert release['metaBeta']['sha256']=='1fbbbd89576659f425920ef9e752e0e20128c0208b8dfdd0beb565f60840a7b9'
assert release['metaBeta']['automatedTest']=='Complete'
assert release['quest']['debuggable'] is False
assert release['quest']['versionCode']==20018
assert release['quest']['certificateSha256']==release['metaBeta']['certificateSha256']
assert release['quest']['sha256']=='5e2954dc7597224f478b6bc3a2c167e785588f08f1d8eb4941f73e4179f1321b'
assert release['quest']['requiresObb'] is False
assert release['quest']['companionUpdateRequired'] is False
assert pages['index.html'].linksById['quest-download']==release['quest']['downloadUrl']
assert pages['index.html'].linksById['meta-beta-invite']==release['metaBeta']['invite']
assert release['legacyQuest']['debuggable'] is True
assert 'STcmVYqeqQ8' in (ROOT/'site.js').read_text()
for p in ROOT.rglob('*'):
    if '.git' in p.parts or '.artifacts' in p.parts:continue
    assert p.suffix.lower() not in ('.pfx','.p12','.key','.apk','.exe'),p
print('PASS: internal links/anchors, heading structure, release identity, consent embed and public file boundaries')
