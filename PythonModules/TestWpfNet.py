"""Test Program to show WPF Windows created with Python.NET"""

# .NET assemblies sometimes have to be imported after the AddReference
# pylint: disable=C0413
import clr
import sys
sys.path.append(r"C:\Program Files (x86)\Reference Assemblies\Microsoft\Framework\.NETFramework\v4.0\Profile\Client")
clr.AddReference("PresentationCore")
clr.AddReference("PresentationFramework")
clr.AddReference("System")
clr.AddReference("WindowsBase")

import System
import System.Windows
import System.Windows.Controls

class MainWindow(System.Windows.Window):
    """Class which represents a WPF main window."""
    def __init__(self):
        self.Width = 300
        self.Height = 300

        grid = System.Windows.Controls.Grid()
        self.Content = grid

        self.Button1 = System.Windows.Controls.Button()
        self.Button1.Content = "Say Hello!"
        self.Button1.Height = 23
        self.Button1.Margin = System.Windows.Thickness(96, 50, 107, 0)
        self.Button1.VerticalAlignment = System.Windows.VerticalAlignment.Top
        self.Button1.Click += System.Windows.RoutedEventHandler(self.Button1Click)
        grid.Children.Add(self.Button1)

        self.Label1 = System.Windows.Controls.Label()
        self.Label1.Margin = System.Windows.Thickness(84, 115, 74, 119)
        grid.Children.Add(self.Label1)

    def Button1Click(self, sender, eventargs):
        """WPF event handler in Python"""
        self.Label1.Content = "Hello WPF"

def WpfStarter():
    """Function which encapsulates the WPF startup code."""
    app = System.Windows.Application()
    app.Run(MainWindow())

def Main():
    """Function to create the WPF environment"""
    domain = System.AppDomain.CreateDomain("WPF Host")
    starter = System.CrossAppDomainDelegate(WpfStarter)
    domain.DoCallBack(starter)
    System.AppDomain.Unload(domain)

if __name__ == "__main__":
    Main()
