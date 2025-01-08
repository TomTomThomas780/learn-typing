; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "打字宝典-Learn Typing"
!define PRODUCT_VERSION "beta 0.0.2"
!define PRODUCT_PUBLISHER "JZH"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\learn_typing.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_STARTMENU_REGVAL "NSIS:StartMenuDir"

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; Language Selection Dialog Settings
!define MUI_LANGDLL_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_LANGDLL_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_LANGDLL_REGISTRY_VALUENAME "NSIS:Language"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; Start menu page
var ICONS_GROUP
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "打字宝典-Learn Typing"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${PRODUCT_STARTMENU_REGVAL}"
!insertmacro MUI_PAGE_STARTMENU Application $ICONS_GROUP
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\learn_typing.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "SimpChinese"
!insertmacro MUI_LANGUAGE "Spanish"
!insertmacro MUI_LANGUAGE "SpanishInternational"
!insertmacro MUI_LANGUAGE "TradChinese"

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "Setup.exe"
InstallDir "$PROGRAMFILES\打字宝典-Learn Typing"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Function .onInit
  !insertmacro MUI_LANGDLL_DISPLAY
FunctionEnd

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite on
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\dist\learn_typing.exe"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\scoreboard.py"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\music.py"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\learn_typing.py"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\heart.py"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\button.py"
  SetOutPath "C:\ProgramData\learn_typing\data"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\data\level_data.json"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\data\level.json"
  SetOutPath "C:\ProgramData\learn_typing\images"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\images\sheet_of_typing.bmp"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\images\heart.bmp"
  SetOutPath "C:\ProgramData\learn_typing\sounds"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\sounds\sucessful_level.wav"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\sounds\sucessful_letter.wav"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\sounds\fail_level.wav"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\sounds\fail_letter.wav"
  File "D:\python\other_programs\my_own_creative\tool\learn_typing\sounds\background.wav"

; Shortcuts
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\打字宝典-Learn Typing.lnk" "$INSTDIR\learn_typing.exe"
  CreateShortCut "$DESKTOP\打字宝典-Learn Typing.lnk" "$INSTDIR\learn_typing.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -AdditionalIcons
  SetOutPath $INSTDIR
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk" "$INSTDIR\uninst.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\learn_typing.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\learn_typing.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) 已成功地从你的计算机移除。"
FunctionEnd

Function un.onInit
!insertmacro MUI_UNGETLANGUAGE
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "你确实要完全移除 $(^Name) ，其及所有的组件？" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  !insertmacro MUI_STARTMENU_GETFOLDER "Application" $ICONS_GROUP
  Delete "$INSTDIR\uninst.exe"
  Delete "C:\ProgramData\learn_typing\sounds\background.wav"
  Delete "C:\ProgramData\learn_typing\sounds\fail_letter.wav"
  Delete "C:\ProgramData\learn_typing\sounds\fail_level.wav"
  Delete "C:\ProgramData\learn_typing\sounds\sucessful_letter.wav"
  Delete "C:\ProgramData\learn_typing\sounds\sucessful_level.wav"
  Delete "C:\ProgramData\learn_typing\images\heart.bmp"
  Delete "C:\ProgramData\learn_typing\images\sheet_of_typing.bmp"
  Delete "C:\ProgramData\learn_typing\data\level.json"
  Delete "C:\ProgramData\learn_typing\data\level_data.json"
  Delete "$INSTDIR\button.py"
  Delete "$INSTDIR\heart.py"
  Delete "$INSTDIR\learn_typing.py"
  Delete "$INSTDIR\music.py"
  Delete "$INSTDIR\scoreboard.py"
  Delete "$INSTDIR\learn_typing.exe"

  Delete "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk"
  Delete "$DESKTOP\打字宝典-Learn Typing.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\打字宝典-Learn Typing.lnk"

  RMDir "C:\ProgramData\learn_typing\sounds"
  RMDir "C:\ProgramData\learn_typing\images"
  RMDir "C:\ProgramData\learn_typing\data"
  RMDir "$SMPROGRAMS\$ICONS_GROUP"
  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd