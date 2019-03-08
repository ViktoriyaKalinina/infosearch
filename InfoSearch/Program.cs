using System;
using System.IO;
using System.Net;

namespace InfoSearch
{
    class Program
    {
        static void Main(string[] args)
        {
            string docPath = @"/Users/visqas/infosearch/web_pages";

            using (StreamWriter outputFile = new StreamWriter(Path.Combine(docPath, "index.txt"), true))
            using (var client = new WebClient())
            {
                for (int i = 1; i <= 100; i++)
                {
                    string remoteUrl = String.Format("http://online-knigi.com/page/196339?page={0}", i);
                    string fileName = String.Format(@"/Users/visqas/infosearch/web_pages/page{0}.html", i);

                    client.DownloadFile(remoteUrl, fileName);

                    outputFile.WriteLine("doc: {0}, url: {1}", i, remoteUrl);
                }
            }
        }
    }
}