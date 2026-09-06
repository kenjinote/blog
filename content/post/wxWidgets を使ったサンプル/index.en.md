---
title: 'Sample using wxWidgets'
slug: "wxWidgets を使ったサンプル"
date: 2023-04-18T00:18:22+09:00
tags: ["wxWidgets", "Sample"]
draft: false
image: "img.png"
categories: ["Programming"]
---

## What is wxWidgets

wxWidgets is a C++ GUI library that works on platforms such as Windows, Mac, Linux, Android, and iOS.

## Installing wxWidgets

1. Open https://www.wxwidgets.org/downloads/ and download the `Windows Installer`.
2. Run `wxMSW-3.2.2.1-Setup.exe` to install.
3. Open "C:\wxWidgets-3.2.2.1\build\msw\wx_vc17.sln" from the installed folder.
4. After opening `wx_vc17.sln`, select `Build` > `Batch Build`.
5. Click the `Select All` button, and then click the Rebuild button.
6. Once the build is finished, temporarily close Visual Studio.

## Creating a Sample Project

1. Open Visual Studio.
2. Select `File` > `New` > `Project`.
3. Select `Windows Desktop Application` (tabs are `C++`, `Windows`, `Desktop`).
4. Enter `wxWidgetsSample` for the `Project Name`.
5. Click `Create`.
6. Right-click `wxWidgetsSample` and select `Properties`.
7. Under `Configuration Properties` > `C/C++` > `Additional Include Directories`, add `C:\wxWidgets-3.2.2.1\include` and `C:\wxWidgets-3.2.2.1\include\msvc`.
8. Under `Configuration Properties` > `Linker` > `Additional Library Directories`, add `C:\wxWidgets-3.2.2.1\lib\vc_x64_lib`.
9. Open `wxWidgetsSample.cpp` and replace it with the code below.
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
10. If you build and run it, a window like the one below will open.

![img_1.png](img_1.png)


## References

The sample project is provided below.
[wxWidgetsSample](https://github.com/kenjinote/wxWidgetsSample)

- [Official Site](https://www.wxwidgets.org)
- [Game using C++ and wxWidgets](https://ken-ohwada.hatenadiary.org/entry/2022/07/14/165213)

That's all.
