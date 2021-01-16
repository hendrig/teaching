using System;
using System.Drawing;
using UtensiliosDomesticos;

namespace Casa
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Programa da casa!");

            var sofa = new Movel();
            sofa.nome = "Sofá Vermelho";
            sofa.cor = ConsoleColor.Red;
            Console.ForegroundColor = sofa.cor;
            Console.WriteLine(sofa.nome);
        }
    }
}
