using System;

namespace Heranca
{
    public class VeiculoAGasolina : Veiculo
    {
        public string MedidaDeConsumo { get; set; }

        public VeiculoAGasolina(string marca, string modelo, string medidaDeConsumo) : base(marca, modelo)
        {
            MedidaDeConsumo = medidaDeConsumo;
        }

        public void CalcularConsumo(int distanciaPercorrida, double combustivelConsumido)
        {
            var consumo = distanciaPercorrida / combustivelConsumido;
            Console.WriteLine(consumo + " " + MedidaDeConsumo);
        }
    }
}