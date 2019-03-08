using System;
using System.Net;

namespace InfoSearch
{
    class Program
    {
        static void Main(string[] args)
        {
            
            new WebClient().DownloadFile("http://google.com", @"C:\Users\visqas\source\repos\InfoSearch\web_pages\page.html");
        }
    }
}
