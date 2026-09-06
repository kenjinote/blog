---


title: "'Ejemplo usando wxWidgets'"
date: 2023-04-18T00:18:22+09:00
tags: ["wxWidgets", "Ejemplo"]
draft: false
image: "img.png"
categories: ["Programación"]
---



## ¿Qué es wxWidgets?

wxWidgets es una biblioteca GUI de C++ que funciona en plataformas como Windows, Mac, Linux, Android, iOS, entre otras.

## Instalación de wxWidgets

1. Abre https://www.wxwidgets.org/downloads/ y descarga `Windows Installer`.
2. Ejecuta `wxMSW-3.2.2.1-Setup.exe` para instalar.
3. Abre "C:\wxWidgets-3.2.2.1\build\msw\wx_vc17.sln" desde la carpeta instalada.
4. Una vez abierto `wx_vc17.sln`, selecciona `Compilar` > `Compilar por lotes` (Build > Batch Build).
5. Haz clic en el botón `Seleccionar todo` y luego en el botón Recompilar.
6. Cierra Visual Studio una vez que finalice la compilación.

## Creación de un proyecto de ejemplo

1. Abre Visual Studio.
2. Selecciona `Archivo` > `Nuevo` > `Proyecto`.
3. Selecciona `Aplicación de escritorio de Windows` (pestañas `C++`, `Windows`, `Escritorio`).
4. Ingresa `wxWidgetsSample` en `Nombre del proyecto`.
5. Haz clic en `Crear`.
6. Haz clic derecho en `wxWidgetsSample` y selecciona `Propiedades`.
7. En `Propiedades de configuración` > `C/C++` > `Directorios de inclusión adicionales`, agrega `C:\wxWidgets-3.2.2.1\include` y `C:\wxWidgets-3.2.2.1\include\msvc`.
8. En `Propiedades de configuración` > `Vinculador` > `Directorios de bibliotecas adicionales`, agrega `C:\wxWidgets-3.2.2.1\lib\vc_x64_lib`.
9. Abre `wxWidgetsSample.cpp` y reemplázalo con el siguiente código.
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
10. Al compilar y ejecutar se abrirá una ventana como la siguiente.

![img_1.png](img_1.png)


## Referencias

El proyecto de ejemplo se encuentra a continuación.
[wxWidgetsSample](https://github.com/kenjinote/wxWidgetsSample)

- [Sitio oficial](https://www.wxwidgets.org)
- [Juegos creados con C++ y wxWidgets](https://ken-ohwada.hatenadiary.org/entry/2022/07/14/165213)

Fin.
