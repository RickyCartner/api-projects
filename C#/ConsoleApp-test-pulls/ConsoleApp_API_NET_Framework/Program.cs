using Newtonsoft.Json;
//using Newtonsoft.Json.Serialization;
//using Newtonsoft.Json.Converters;
//using Newtonsoft.Json.Linq;
using System;
using System.Net.Http;
using System.Collections.Generic;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

namespace ConsoleApp_API_NET_Framework
{

    public class Program
    {
        static void Main(string[] args)
        {
            using (var client = new HttpClient())
            {
                var endpoint = new Uri("https://jsonplaceholder.typicode.com/posts");
                var response = client.GetAsync(endpoint).Result;
                var json = response.Content.ReadAsStringAsync().Result;
                //Console.WriteLine(json);
                //Console.ReadLine();

                
                List<MyJsonClass> myJsonObject = JsonConvert.DeserializeObject<List<MyJsonClass>>(json);

                foreach (var item in myJsonObject)
                {
                    Console.WriteLine(item.id);
                    Console.WriteLine(item.title);
                }
                //Console.WriteLine(myJsonObject[0].id);
                //Console.WriteLine(myJsonObject[0].title);
                //Console.WriteLine(myJsonObject[1].id);
                //Console.WriteLine(myJsonObject[1].title);
                Console.ReadLine();

                /********************/
                /* Custom list read */
                /********************/
                //var get_jsonString = @"[{'First_Name': 'Ricky', 'Last_Name': 'Cartner'}]";
                ////Use of the method
                ////var result = JsonConvert.DeserializeObject<UserDetails>(get_jsonString);
                //List<UserDetails> result = JsonConvert.DeserializeObject<List<UserDetails>>(get_jsonString);
                
                ////Console.WriteLine("JSON-Parse Method\n");
                //Console.WriteLine(string.Concat("\nDisplaying First and Last Name, ", result[0].First_Name, " " + result[0].Last_Name, "."));
                //Console.ReadLine();
            }

        }

        
    }
}
