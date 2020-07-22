using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace playfair1
{
    public class Playfair
    {
        protected string[] Matrix = new string[27];
        private readonly string[] _alphabet = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
        private const int Lines = 6;
        private const int Columns = 5;

        public void CreateMatrix(string passPhrase)
        {
            // Check if there is repeated letters
            var passPhraseArray = Regex.Split(passPhrase.ToUpper().Trim(), string.Empty)
                                        .Where(c => !string.IsNullOrEmpty(c))
                                        .Distinct()
                                        .ToArray();

            // Remove passPhrase letters from alphabet array
            var remainingAlphabet = this._alphabet.Where(c => !passPhraseArray.Contains(c)).ToArray();

            // Add passPhrase letters in the beginning of the matrix
            var lastIterator = 0;
            for(var i = 0; i < passPhraseArray.Length; i++){
                this.Matrix[i] = passPhraseArray[i];
                lastIterator++;
            }

            // Add the rest of the alphabet on the matrix
            foreach (var t in remainingAlphabet)
            {
                this.Matrix[lastIterator] = t;
                lastIterator++;
            }

            // Print 
            for(var i = 0; i<Lines;i++){
                var line = "";
                for(var j = 0; j<Columns; j++)
                {
                    var index = i * Columns + j;
                    if (index < this.Matrix.Length)
                    {
                        line += Matrix[index] + " ";
                    }
                }
                System.Console.WriteLine(line);
            }
        }

        public string EncodeDecodeText(string phrase)
        {
            Console.WriteLine("Encoding...");
            var trimmed = string.Concat(phrase.Where(c => !char.IsWhiteSpace(c)));
            var textToEncrypt = Regex.Split(trimmed.ToUpper().Trim(), string.Empty)
                                    .Where(c => !string.IsNullOrEmpty(c))
                                    .ToList();

            if (textToEncrypt.Count % 2 != 0)
            {
                textToEncrypt.Add("X");
            }

            var encodedText = "";
            for (var i = 0; i < textToEncrypt.Count; i += 2)
            {
                //find the line and column of the pair of letters
                var letter1Index = this.Matrix.ToList().IndexOf(textToEncrypt[i]);
                var letter2Index = this.Matrix.ToList().IndexOf(textToEncrypt[i+1]);
                // get the letters on that opposite pair
                var column1 = (int)letter1Index % Columns;
                var line1 = letter1Index / Columns;
                var column2 = (int)letter2Index % Columns;
                var line2 = letter2Index / Columns;
                // rule: same line, other letter column
                var letter1 = this.Matrix[line1 * Columns + column2];
                var letter2 = this.Matrix[line2 * Columns + column1];
                // add them on the decoded text.
                encodedText += letter1 + letter2 + " ";
            }

            Console.WriteLine(encodedText);
            return encodedText;
        }
    }
}