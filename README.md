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
managed private Beta channel for Quest 3/3S. The accepted development-signed APK
remains available only as a technical fallback.

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
