---
title: "Exemple utilisant wxWidgets"
slug: "wxWidgets を使ったサンプル"
date: 2023-04-18T00:18:22+09:00
tags: ["wxWidgets", "Exemple"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

## Qu'est-ce que wxWidgets

wxWidgets est une bibliothèque GUI C++ qui fonctionne sur des plateformes telles que Windows, Mac, Linux, Android, iOS, etc.

## Installation de wxWidgets

1. Ouvrez https://www.wxwidgets.org/downloads/ et téléchargez le `Windows Installer`.
2. Exécutez `wxMSW-3.2.2.1-Setup.exe` pour l'installer.
3. Ouvrez "C:\wxWidgets-3.2.2.1\build\msw\wx_vc17.sln" à partir du dossier installé.
4. Après avoir ouvert `wx_vc17.sln`, sélectionnez `Générer` > `Générer par lots`.
5. Appuyez sur le bouton `Sélectionner tout`, puis sur le bouton `Régénérer`.
6. Une fois la compilation terminée, fermez temporairement Visual Studio.

## Création du projet d'exemple

1. Ouvrez Visual Studio.
2. Sélectionnez `Fichier` > `Nouveau` > `Projet`.
3. Sélectionnez `Application de bureau Windows` (les onglets sont `C++`, `Windows`, `Bureau`).
4. Entrez `wxWidgetsSample` dans `Nom du projet`.
5. Cliquez sur `Créer`.
6. Faites un clic droit sur `wxWidgetsSample` et sélectionnez `Propriétés`.
7. Dans `Propriétés de configuration` > `C/C++` > `Autres répertoires Include`, ajoutez `C:\wxWidgets-3.2.2.1\include` et `C:\wxWidgets-3.2.2.1\include\msvc`.
8. Dans `Propriétés de configuration` > `Éditeur de liens` > `Répertoires de bibliothèques supplémentaires`, ajoutez `C:\wxWidgets-3.2.2.1\lib\vc_x64_lib`.
9. Ouvrez `wxWidgetsSample.cpp` et remplacez-le par le code ci-dessous.
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
10. Lors de la compilation et de l'exécution, une fenêtre comme celle ci-dessous s'ouvrira.

![img_1.png](img_1.png)


## Références

Le projet d'exemple est disponible ci-dessous.
[wxWidgetsSample](https://github.com/kenjinote/wxWidgetsSample)

- [Site officiel](https://www.wxwidgets.org)
- [Jeux utilisant C++ et wxWidgets](https://ken-ohwada.hatenadiary.org/entry/2022/07/14/165213)

C'est tout.
