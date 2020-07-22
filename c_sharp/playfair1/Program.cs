using System;

namespace playfair1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("The playfair program. Write the passphrase");
            var pass = Console.ReadLine();
            Playfair p = new Playfair();

            p.CreateMatrix(pass);

            Console.WriteLine("Type the text to be encoded");
            var text = Console.ReadLine();
            var encoded = p.EncodeDecodeText(text);
            var decoded = p.EncodeDecodeText(encoded);
        }
    }
}
