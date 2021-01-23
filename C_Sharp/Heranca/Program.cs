namespace Heranca
{
    public static class Program
    {
        static void Main(string[] args)
        {
            var veiculoAGasolina = new VeiculoAGasolina("Honda", "Civic", "Km/l");
            var veiculoAGas = new VeiculoAGas("Fiat", "Siena", "Km/m3");

            veiculoAGasolina.CalcularConsumo(140, 13.5);
            veiculoAGas.CalcularConsumo(140, 10);
        }
    }
}