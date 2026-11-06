# XPPanelsVR for Quest · Mac and Windows Companion

Public download/setup website: https://aldomm.github.io/XPPanelsVR-Quest/

This repository contains only the static website, public release metadata and
notices. Application source repositories remain private. No signing private key,
credentials, aircraft files or simulator SDK belong here.

The release is a complete matched beta bundle, not a partial preview. The Windows
Companion uses a consistent self-signed identity and published hashes; Windows does
not automatically trust independently self-signed publishers. The Apple-silicon Mac
Companion is Developer ID signed, Apple-notarized and stapled, and the sister
XPPanelsVR application for Apple Vision Pro has been accepted by Apple. The primary Quest
distribution is production-signed, non-debuggable and installed through Meta’s
managed private Beta channel for Quest 3/3S. The latest direct Quest APK is also production-signed and can update an earlier
production-signed installation in place. Older development-signed APKs remain
archived; they are not the current website download.

The normal connection uses USB forwarding and computer-local services. Optional
Wi-Fi fallback is designed for a user-approved trusted private LAN. These local
transports are not internet-facing encrypted pairing services and must never be
port-forwarded or exposed to the public internet.

GitHub Pages serves `main` at the repository root. Large downloads are release
assets, not committed binaries. See the website for setup and current limitations.

The supplied demonstration is https://youtu.be/STcmVYqeqQ8 and loads only after
an explicit click on the website. The hero image is a cropped still at approximately 6:16 from the project owner’s demo: https://youtu.be/STcmVYqeqQ8. It is stored locally so viewing the page does not contact YouTube.

Windows 0.2.1-beta.1 adds only explicit plugin setup. Economy media and cockpit
protocols are unchanged and compatible with Meta Quest beta 0.2.0-beta.1/code 20002.
Mac Companion remains 0.2.0-beta.1. Higher-quality Windows video was withdrawn.

The website header, favicon and Quest download card use the original Apple Vision Pro
XPPanelsVR app artwork from Publishing/CompanionWebsite/assets/app-icon.png in the
private VR repository (SHA256 9d41bece1dff8150ad3cbc3f425e6fb6d8d9fc6d643a572b6edccc2e4a66af41).

Setup instructions refreshed 15 October 2026 after reading the Mac package handover
and verifying the published PKG digest. The guide covers both OS installers, bundled
plugin setup, optional Mac virtual monitor, Meta approval, USB authorization, nine
display sources, optional media, first-session checks, recovery and rollback.
Windows live acceptance now includes sampled both-side controls, ISCS and audio
on Meta beta code 20002; this does not establish every PC/aircraft combination.

Quest Beta 2 / build 20018 is published as the latest direct APK on 5 November 2026.
It improves fixed cockpit printing and restores the original moving pitch-trim
scales with fixed reference arrows. Companion binaries and protocols are unchanged.
The Meta channel is separate; this publication does not upload or promote a Meta
build. Current APK details and checksum are in release.json.

## Anonymous page-view and download analytics

All downloads stay public on GitHub. No email, registration, sign-in or payment is required.
The anonymous counters use the existing Cloudflare Workers Free endpoint and D1
Free database. An analytics failure or
quota limit never controls or delays the direct download link.

The private owner report separates website download-link requests (by UTC day/hour,
immutable release asset ID, file/version, platform and approximate country) from
GitHub per-asset download_count totals. Neither means completed downloads, installs,
unique people or bot-free traffic. Direct GitHub links bypass website tracking;
VPNs/proxies can change the apparent country. No email, account ID, raw IP,
fingerprint or tracking cookie is stored by the counter. Providers may process
connection information under their own terms.

`page-views.js` counts one load per landing-page document, including repeat loads;
it does not identify unique visitors. Only the repository root and `index.html`
qualify. Daily/hourly aggregates contain product, approximate country, time bucket
and count, with no referrer, query string, raw IP or persistent visitor identifier.
Page-view tracking begins with the first accepted event and is never backfilled.

The existing hosted daily report uses a fixed 09:00 Asia/Hong_Kong cutoff and shows
24-hour, 7-day, 30-day and all-time page views separately from downloads. Partial
history is labeled. Only package-download activity in the latest fully covered
24-hour window can qualify an email to the owner; page views alone never do.

The previous auth-service draft is superseded and must not be deployed. The current
setup, free limits and private report commands are documented in the Companion
repository's analytics-service/README.md. No R2, Supabase, SMTP, paid plan or domain
purchase is involved. Optional support remains aldoapps@gmail.com.

## Windows icon installer — 5 November 2026

Windows Quest Companion 0.3.0-beta.1 preserves the current separated 0.3.0-preview.1
payload and adds only installer branding from icon commit 52a1c2f, cherry-picked
onto the current Quest separation checkpoint a845076. The older handover's suggested
0.2.2 was not used because the PC had already advanced to 0.3.0 product separation.
The Mac installer, Quest production APK code 20018 and Meta beta code 20002 are
unchanged. All previous releases remain available. The Windows package has its own
Quest launcher, plugin and settings; see the setup guide for older shared installs.

## Quest panel corrections — 5 November 2026

Latest direct production APK: build 20019 / 0.2.0-beta.2-panel-fixes, accepted in-headset by the author. Includes transponder label/window clearance, native knob alignment, GCS/ATC FAIL placement and offline brake needle preview. Windows 0.3.0-beta.1, Mac installer, download-count script and Meta channel remain unchanged.
