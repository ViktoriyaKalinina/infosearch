using System;
using System.IO;
using System.Net;
using HtmlAgilityPack;

namespace InfoSearch
{
    class Program
    {
        static void Main(string[] args)
        {
            string docPath = @"/Users/visqas/infosearch/web_pages";
            string resultDoc;

            HtmlDocument htmlDoc = new HtmlDocument();

            int counter = 100;
            for (int i = 1; i <= counter; i++)
            {
                string remoteUrl = String.Format("http://online-knigi.com/page/196339?page={0}", i);
                string fileName = String.Format(@"/Users/visqas/infosearch/web_pages/{0}page.txt", i);

                var request = (HttpWebRequest)WebRequest.Create(remoteUrl);
                request.Method = "GET";

                using (StreamWriter outputFile = new StreamWriter(Path.Combine(docPath, "index.txt"), true))
                using (StreamWriter file = new StreamWriter(fileName))
                using (var response = (HttpWebResponse)request.GetResponse())
                using (var stream = response.GetResponseStream())
                {
                    htmlDoc.Load(stream);
                    resultDoc = htmlDoc.DocumentNode.SelectSingleNode("//*[@id=\"content\"]/div[2]/div/div[3]").InnerText;

                    file.WriteLine(resultDoc);
                    outputFile.WriteLine("doc: {0}, url: {1}", i, remoteUrl);
                }
            }
        }
    }
}