# Conceitos de Programação Orientada a Objeto: Herança

Herança é um princípio de orientação a objetos, que permite que classes compartilhem atributos e métodos, através de "heranças". Ela é usada na intenção de reaproveitar código ou comportamento generalizado ou especializar operações ou atributos

Em C# utiliza-se a seguinte sintaxe para se utilizar herança:

```csharp
public class ClassePai
{
    public ClassePai(string atributo);
}

public class ClasseFilha : ClassePai
{
    public string OutroAtributo;
    public ClasseFilha(string atributo, string outroAtributo)
        : base(atributo)
    {
        OutroAtributo = outroAtributo;
    }
}
```