---
title: "Exemplo usando wxWidgets"
slug: "wxWidgets を使ったサンプル"
date: 2023-04-18T00:18:22+09:00
tags: ["wxWidgets", "Exemplo"]
draft: false
image: "img.png"
categories: ["Programação"]
---

## O que é wxWidgets

wxWidgets é uma biblioteca GUI C++ que funciona em plataformas como Windows, Mac, Linux, Android, iOS, etc.

## Instalação do wxWidgets

1. Abra https://www.wxwidgets.org/downloads/ e baixe o `Windows Installer`.
2. Execute `wxMSW-3.2.2.1-Setup.exe` para instalar.
3. Abra "C:\wxWidgets-3.2.2.1\build\msw\wx_vc17.sln" a partir da pasta instalada.
4. Após abrir `wx_vc17.sln`, selecione `Build` > `Batch Build`.
5. Pressione o botão `Select All` e, em seguida, o botão `Rebuild`.
6. Após a conclusão da compilação, feche o Visual Studio temporariamente.

## Criação do projeto de exemplo

1. Abra o Visual Studio.
2. Selecione `File` > `New` > `Project`.
3. Selecione `Windows Desktop Application` (as guias são `C++`, `Windows`, `Desktop`).
4. Insira `wxWidgetsSample` em `Project name`.
5. Clique em `Create`.
6. Clique com o botão direito em `wxWidgetsSample` e selecione `Properties`.
7. Em `Configuration Properties` > `C/C++` > `Additional Include Directories`, adicione `C:\wxWidgets-3.2.2.1\include` e `C:\wxWidgets-3.2.2.1\include\msvc`.
8. Em `Configuration Properties` > `Linker` > `Additional Library Directories`, adicione `C:\wxWidgets-3.2.2.1\lib\vc_x64_lib`.
9. Abra `wxWidgetsSample.cpp` e substitua pelo código abaixo.
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
10. Ao compilar e executar, uma janela como a abaixo será aberta.

![img_1.png](img_1.png)


## Referências

O projeto de exemplo está disponível abaixo.
[wxWidgetsSample](https://github.com/kenjinote/wxWidgetsSample)

- [Site oficial](https://www.wxwidgets.org)
- [Jogos usando C++ e wxWidgets](https://ken-ohwada.hatenadiary.org/entry/2022/07/14/165213)

É isso.
