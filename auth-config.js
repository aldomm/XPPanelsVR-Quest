// Shared email verification and download worker. Keep disabled until configured and private assets are migrated.
window.XPPanelsAuthConfig = {
  enabled: false,
  productName: 'Meta Quest Companion and Quest app',
  supabaseUrl: '',
  supabaseAnonKey: '',
  workerUrl: '',
  privacyUrl: 'notices.html',
  assets: {
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.3.0-beta.1/XPPanelsQuestCompanion-0.3.0-beta.1-windows-x64-SELF-SIGNED.exe': 'quest-win-0.3.0',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.3.0-beta.1/AldoApps-Preview-Signing.cer': 'quest-win-signing-certificate',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.3.0-beta.1/SHA256SUMS.txt': 'quest-win-checksums',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.2.1-beta.1/XPPanels-Companion-0.2.1-beta.1-windows-x64-SELF-SIGNED.exe': 'quest-win-0.2.1',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.2.0-beta.1/XPPanels-Companion-0.2.0-beta.1-windows-x64-SELF-SIGNED.exe': 'quest-win-0.2.0',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.2.0-preview.1/XPPanels-Companion-0.2.0-preview.1-windows-x64-SELF-SIGNED.exe': 'quest-win-preview',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.2.0-beta.1/XPPanels-Companion-0.2.0-beta.1-macos-arm64.pkg': 'quest-mac-0.2.0',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.2.0-preview.1/XPPanels-Companion-0.2.0-preview.1-macos-arm64.pkg': 'quest-mac-preview',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.2.0-beta.2-code20019/XPPanelsVR-Quest-0.2.0-beta.2-panel-fixes-code20019-release.apk': 'quest-apk-0.2.0-beta2',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.2.0-beta.2-code20018/XPPanelsVR-Quest-0.2.0-beta.2-trim-pointers-code20018-release.apk': 'quest-apk-0.2.0-beta2-20018',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.2.0-beta.1/XPPanelsVR-Quest-2026.10.14-beta.1.apk': 'quest-apk-0.2.0-beta1',
    'https://github.com/aldomm/XPPanelsVR-Quest/releases/download/v0.2.0-preview.1/XPPanelsVR-Quest-2026.10.14-preview.apk': 'quest-apk-preview',
  },
};
