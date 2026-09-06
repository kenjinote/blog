---
title: "Contoh menggunakan wxWidgets"
slug: "wxWidgets を使ったサンプル"
date: 2023-04-18T00:18:22+09:00
tags: ["wxWidgets", "サンプル"]
draft: false
image: "img.png"
categories: ["プログラミング"]
---

## Apa itu wxWidgets

wxWidgets adalah pustaka GUI C++ yang berjalan di berbagai platform seperti Windows, Mac, Linux, Android, dan iOS.

## Instalasi wxWidgets

1. Buka https://www.wxwidgets.org/downloads/ dan unduh `Windows Installer`.
2. Jalankan `wxMSW-3.2.2.1-Setup.exe` untuk menginstal.
3. Dari folder instalasi, buka "C:\wxWidgets-3.2.2.1\build\msw\wx_vc17.sln".
4. Setelah membuka `wx_vc17.sln`, pilih `Build` > `Batch Build`.
5. Klik tombol `Select All`, lalu klik tombol `Rebuild`.
6. Setelah build selesai, tutup Visual Studio sementara waktu.

## Membuat Proyek Sampel

1. Buka Visual Studio.
2. Pilih `File` > `New` > `Project`.
3. Pilih `Windows Desktop Application` (Tab `C++`, `Windows`, `Desktop`).
4. Masukkan `wxWidgetsSample` pada `Project name`.
5. Klik `Create`.
6. Klik kanan pada `wxWidgetsSample` dan pilih `Properties`.
7. Tambahkan `C:\wxWidgets-3.2.2.1\include` dan `C:\wxWidgets-3.2.2.1\include\msvc` ke `Configuration Properties` > `C/C++` > `Additional Include Directories`.
8. Tambahkan `C:\wxWidgets-3.2.2.1\lib\vc_x64_lib` ke `Configuration Properties` > `Linker` > `Additional Library Directories`.
9. Buka `wxWidgetsSample.cpp` dan ganti dengan kode berikut.
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
10. Saat Anda build dan jalankan, jendela seperti ini akan terbuka.

![img_1.png](img_1.png)


## Referensi

Proyek sampel disediakan di bawah ini.
[wxWidgetsSample](https://github.com/kenjinote/wxWidgetsSample)

- [Situs Resmi](https://www.wxwidgets.org)
- [Permainan menggunakan C++ dan wxWidgets](https://ken-ohwada.hatenadiary.org/entry/2022/07/14/165213)

Sekian.

