---


title: "'wxWidgets를 사용한 샘플'"
date: 2023-04-18T00:18:22+09:00
tags: ["wxWidgets", "샘플"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---



## wxWidgets란

wxWidgets는 Windows, Mac, Linux, Android, iOS 등의 플랫폼에서 동작하는 C++ GUI 라이브러리입니다.

## wxWidgets 설치

1. https://www.wxwidgets.org/downloads/ 를 열어 `Windows Installer`를 다운로드합니다.
2. `wxMSW-3.2.2.1-Setup.exe`를 실행하여 설치합니다.
3. 설치된 폴더에서 "C:\wxWidgets-3.2.2.1\build\msw\wx_vc17.sln"을 엽니다.
4. `wx_vc17.sln`을 열고 `빌드`＞`일괄 빌드`를 선택합니다.
5. `모두 선택` 버튼을 누르고, 리빌드 버튼을 누릅니다.
6. 빌드가 완료되면 일단 Visual Studio를 닫습니다.

## 샘플 프로젝트 생성

1. Visual Studio를 엽니다.
2. `파일`＞`새로 만들기`＞`프로젝트`를 선택합니다.
3. `Windows 데스크톱 애플리케이션` (탭이 `C++`, `Windows`, `데스크톱`)을 선택합니다.
4. `프로젝트 이름`에 `wxWidgetsSample`을 입력합니다.
5. `만들기`를 클릭합니다.
6. `wxWidgetsSample`을 우클릭하고 `속성`을 선택합니다.
7. `구성 속성`＞`C/C++`＞`추가 포함 디렉터리`에 `C:\wxWidgets-3.2.2.1\include`와 `C:\wxWidgets-3.2.2.1\include\msvc`를 추가합니다.
8. `구성 속성`＞`링커`＞`추가 라이브러리 디렉터리`에 `C:\wxWidgets-3.2.2.1\lib\vc_x64_lib`를 추가합니다.
9. `wxWidgetsSample.cpp`를 열고 다음 코드로 교체합니다.
```cpp
#pragma comment(linker,"\"/manifestdependency:type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='*' publicKeyToken='6595b64144ccf1df' language='*'\"")

#include <wx/wxprec.h>

#ifndef WX_PRECOMP
#include <wx/wx.h>
#endif

class MyApp : public wxApp
{
public:
	virtual bool OnInit();
};

class MyFrame : public wxFrame
{
public:
	MyFrame();
private:
	void OnHello(wxCommandEvent& event);
	void OnExit(wxCommandEvent& event);
	void OnAbout(wxCommandEvent& event);
};

enum
{
	ID_Hello = 1
};

wxIMPLEMENT_APP(MyApp);

bool MyApp::OnInit()
{
	MyFrame* frame = new MyFrame();
	frame->Show(true);
	return true;
}

MyFrame::MyFrame()
	: wxFrame(NULL, wxID_ANY, "Hello World")
{
	wxMenu* menuFile = new wxMenu;
	menuFile->Append(ID_Hello, "&Hello...\tCtrl-H",
		"Help string shown in status bar for this menu item");
	menuFile->AppendSeparator();
	menuFile->Append(wxID_EXIT);
	wxMenu* menuHelp = new wxMenu;
	menuHelp->Append(wxID_ABOUT);
	wxMenuBar* menuBar = new wxMenuBar;
	menuBar->Append(menuFile, "&File");
	menuBar->Append(menuHelp, "&Help");
	SetMenuBar(menuBar);

	wxButton* button1 = new wxButton(this, ID_Hello, _("Hello"), wxPoint(20, 20), wxSize(100, 32));
	Connect(ID_Hello, wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler(MyFrame::OnHello));

	wxButton* button2 = new wxButton(this, wxID_ABOUT, _("About"), wxPoint(20, 60), wxSize(100, 32));
	Connect(wxID_ABOUT, wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler(MyFrame::OnAbout));

	wxButton* button3 = new wxButton(this, wxID_EXIT, _("Exit"), wxPoint(20, 100), wxSize(100, 32));
	Connect(wxID_EXIT, wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler(MyFrame::OnExit));

	CreateStatusBar();
	SetStatusText("Welcome to wxWidgets!");
	Bind(wxEVT_MENU, &MyFrame::OnHello, this, ID_Hello);
	Bind(wxEVT_MENU, &MyFrame::OnAbout, this, wxID_ABOUT);
	Bind(wxEVT_MENU, &MyFrame::OnExit, this, wxID_EXIT);
}

void MyFrame::OnExit(wxCommandEvent& event)
{
	Close(true);
}

void MyFrame::OnAbout(wxCommandEvent& event)
{
	wxMessageBox("This is a wxWidgets' Hello world sample",
		"About Hello World", wxOK | wxICON_INFORMATION);
}

void MyFrame::OnHello(wxCommandEvent& event)
{
	wxLogMessage("Hello world from wxWidgets!");
}
```
10. 빌드하고 실행하면 아래와 같은 창이 열립니다.

![img_1.png](img_1.png)


## 참고

샘플 프로젝트를 아래에 올려두었습니다.
[wxWidgetsSample](https://github.com/kenjinote/wxWidgetsSample)

- [공식 사이트](https://www.wxwidgets.org)
- [C++와 wxWidgets를 사용한 게임](https://ken-ohwada.hatenadiary.org/entry/2022/07/14/165213)

이상입니다.
