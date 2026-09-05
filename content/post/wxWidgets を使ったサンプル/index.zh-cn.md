---
title: '使用 wxWidgets 的示例'
date: 2023-04-18T00:18:22+09:00
tags: ["wxWidgets", "示例"]
draft: false
image: "img.png"
categories: ["编程"]
---

## 什么是 wxWidgets

wxWidgets 是一个在 Windows、Mac、Linux、Android、iOS 等平台上运行的 C++ GUI 库。

## 安装 wxWidgets

1. 打开 https://www.wxwidgets.org/downloads/ 并下载 `Windows Installer`。
2. 运行 `wxMSW-3.2.2.1-Setup.exe` 进行安装。
3. 从安装目录中打开 "C:\wxWidgets-3.2.2.1\build\msw\wx_vc17.sln"。
4. 打开 `wx_vc17.sln` 后，选择“生成”＞“批生成”。
5. 点击“全选”按钮，然后点击“重新生成”按钮。
6. 生成结束后，先关闭 Visual Studio。

## 创建示例项目

1. 打开 Visual Studio。
2. 选择“文件”＞“新建”＞“项目”。
3. 选择“Windows 桌面应用程序”（标签为 `C++`、`Windows`、`桌面`）。
4. 在“项目名称”中输入 `wxWidgetsSample`。
5. 点击“创建”。
6. 右键点击 `wxWidgetsSample`，选择“属性”。
7. 在“配置属性”＞“C/C++”＞“附加包含目录”中添加 `C:\wxWidgets-3.2.2.1\include` 和 `C:\wxWidgets-3.2.2.1\include\msvc`。
8. 在“配置属性”＞“链接器”＞“附加库目录”中添加 `C:\wxWidgets-3.2.2.1\lib\vc_x64_lib`。
9. 打开 `wxWidgetsSample.cpp` 并将其替换为以下代码。
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
10. 编译并运行后，将打开如下窗口。

![img_1.png](img_1.png)


## 参考

示例项目已上传至以下地址。
[wxWidgetsSample](https://github.com/kenjinote/wxWidgetsSample)

- [官方网站](https://www.wxwidgets.org)
- [使用 C++ 和 wxWidgets 制作的游戏](https://ken-ohwada.hatenadiary.org/entry/2022/07/14/165213)

完毕。
