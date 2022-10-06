using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp_API_NET_Framework
{
    [Serializable]
    public class MyJsonClass
    {
        public int userId { get; set; }
        public int id { get; set; }
        public string title { get; set; }
        public string body { get; set; }

    }
    public class UserDetails
    {
        public string First_Name { get; set; }
        public string Last_Name { get; set; }
    }
}
