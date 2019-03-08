using System;
using System.Net;

namespace InfoSearch
{
    class Program
    {
        static void Main(string[] args)
        {

            string remoteUrl = "https://iknigi.net/avtor-arkadiy-i-boris-strugackie/171272-sobranie-sochineniy-tom-5-19671968-arkadiy-i-boris-strugackie/read/page-1.html";
            string fileName = @"/Users/visqas/infosearch/web_pages/page2.html";

            new WebClient().DownloadFile(remoteUrl, fileName);

            //            using (var client = new WebClient())
            //                {
            //                    for(int i = 1; i <= 10; i++)
            //                        {  
            //                            client.DownloadFile(url + i, @"/Users/visqas/infosearch/web_pages/page{i}");
            //                        }
        }
    }
}