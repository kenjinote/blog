---
title: "使用 wxWidgets 的範例"
slug: "wxWidgets を使ったサンプル"
date: 2023-04-18T00:18:22+09:00
tags: ["wxWidgets", "範例"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

## 什麼是 wxWidgets

wxWidgets 是一個 C++ 的 GUI 函式庫，支援 Windows、Mac、Linux、Android、iOS 等多個平台。

## 安裝 wxWidgets

1. 開啟 https://www.wxwidgets.org/downloads/ 並下載 `Windows Installer`。
2. 執行 `wxMSW-3.2.2.1-Setup.exe` 進行安裝。
3. 從安裝的資料夾中開啟 "C:\wxWidgets-3.2.2.1\build\msw\wx_vc17.sln"。
4. 開啟 `wx_vc17.sln` 後，選擇 `建置` ＞ `批次建置`。
5. 按下 `全選` 按鈕，然後按下 `重建` 按鈕。
6. 建置完成後，暫時關閉 Visual Studio。

## 建立範例專案

1. 開啟 Visual Studio。
2. 選擇 `檔案` ＞ `新增` ＞ `專案`。
3. 選擇 `Windows 桌面應用程式`（分頁為 `C++`、`Windows`、`桌面`）。
4. 在 `專案名稱` 輸入 `wxWidgetsSample`。
5. 點擊 `建立`。
6. 右鍵點擊 `wxWidgetsSample`，選擇 `屬性`。
7. 在 `組態屬性` ＞ `C/C++` ＞ `其他包含目錄` 中新增 `C:\wxWidgets-3.2.2.1\include` 和 `C:\wxWidgets-3.2.2.1\include\msvc`。
8. 在 `組態屬性` ＞ `連結器` ＞ `其他程式庫目錄` 中新增 `C:\wxWidgets-3.2.2.1\lib\vc_x64_lib`。
9. 開啟 `wxWidgetsSample.cpp` 並替換為以下程式碼。
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
10. 建置並執行後，會開啟如下的視窗。

![img_1.png](img_1.png)


## 參考資料

範例專案已上傳至以下連結。
[wxWidgetsSample](https://github.com/kenjinote/wxWidgetsSample)

- [官方網站](https://www.wxwidgets.org)
- [使用 C++ 與 wxWidgets 的遊戲](https://ken-ohwada.hatenadiary.org/entry/2022/07/14/165213)

以上。
