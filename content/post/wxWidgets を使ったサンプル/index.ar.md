---
title: "مثال باستخدام wxWidgets"
slug: "wxWidgets を使ったサンプル"
date: 2023-04-18T00:18:22+09:00
tags: ["wxWidgets", "サンプル"]
draft: false
image: "img.png"
categories: ["プログラミング"]
---

## ما هو wxWidgets

wxWidgets هي مكتبة واجهة مستخدم رسومية بلغة C++ تعمل على أنظمة أساسية مثل Windows و Mac و Linux و Android و iOS.

## تثبيت wxWidgets

1. افتح https://www.wxwidgets.org/downloads/ وقم بتنزيل `Windows Installer`.
2. قم بتشغيل `wxMSW-3.2.2.1-Setup.exe` للتثبيت.
3. من المجلد المثبت، افتح "C:\wxWidgets-3.2.2.1\build\msw\wx_vc17.sln".
4. بعد فتح `wx_vc17.sln` ، حدد `Build` > `Batch Build`.
5. انقر فوق الزر `Select All` ثم انقر فوق الزر `Rebuild`.
6. بمجرد اكتمال البناء، أغلق Visual Studio مؤقتاً.

## إنشاء مشروع مثال

1. افتح Visual Studio.
2. حدد `File` > `New` > `Project`.
3. حدد `Windows Desktop Application` (العلامات هي `C++`، `Windows`، `Desktop`).
4. أدخل `wxWidgetsSample` في `Project name`.
5. انقر على `Create`.
6. انقر بزر الماوس الأيمن على `wxWidgetsSample` وحدد `Properties`.
7. أضف `C:\wxWidgets-3.2.2.1\include` و `C:\wxWidgets-3.2.2.1\include\msvc` إلى `Configuration Properties` > `C/C++` > `Additional Include Directories`.
8. أضف `C:\wxWidgets-3.2.2.1\lib\vc_x64_lib` إلى `Configuration Properties` > `Linker` > `Additional Library Directories`.
9. افتح `wxWidgetsSample.cpp` واستبدله بالكود أدناه.
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
10. عند البناء والتشغيل، ستفتح نافذة مثل هذه.

![img_1.png](img_1.png)


## مراجع

يتم توفير مشروع المثال أدناه.
[wxWidgetsSample](https://github.com/kenjinote/wxWidgetsSample)

- [الموقع الرسمي](https://www.wxwidgets.org)
- [لعبة باستخدام C++ و wxWidgets](https://ken-ohwada.hatenadiary.org/entry/2022/07/14/165213)

هذا كل شيء.

