"""Static website checks: internal links, release metadata and safe public files."""
from html.parser import HTMLParser
from pathlib import Path
import json
from urllib.parse import urlsplit,unquote

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=set();self.links=[];self.headings=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids,'Duplicate anchor'
            self.ids.add(attrs['id'])
        if tag=='a':self.links.append(attrs.get('href',''))
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
assert release['version']=='0.2.0-beta.1'
assert release['channel']=='public beta'
assert release['binaryChangesFromPromotedBuild'] is False
assert release['windows']['signing']=='Self-signed; not automatically trusted by Windows'
assert release['mac']['architecture']=='arm64'
assert release['mac']['sha256']=='13bca320ea205987c8a7cc3373f8d5e2f8def5d8b054d5b890c5709fca14ec2a'
assert release['mac']['notarization']=='Accepted and stapled'
assert release['quest']['debuggable'] is True
assert release['quest']['sha256']=='909fcb79d275d1d95f582e6957e784c58f66ca66226a2e30894ee0bda768a357'
assert 'STcmVYqeqQ8' in (ROOT/'site.js').read_text()
for p in ROOT.rglob('*'):
    if '.git' in p.parts or '.artifacts' in p.parts:continue
    assert p.suffix.lower() not in ('.pfx','.p12','.key','.apk','.exe'),p
print('PASS: internal links/anchors, heading structure, release identity, consent embed and public file boundaries')
