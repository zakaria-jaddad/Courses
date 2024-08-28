const unicode = document.getElementById('uni-input');


// unicode to decimal
// these are global variables 
const decimal = document.getElementById('dec-output');
const binary = document.getElementById('bin-output');
const hex = document.getElementById('hex-output');

// 
try{


    unicode.addEventListener('input', function(){
        let final_result = 0;
        let bin_final_result = "";
        let hex_final_result = ""
        let string = unicode.value;

        // iterating onec at a time 
        for (let i = 0; i < string.length; i+=2){
            // getting the code point 
            let str = string.codePointAt(i)
            let decimal = str.toString(10)
            final_result += decimal;
            final_result += ' ';
            final_result += String.fromCodePoint(Number(decimal))
            final_result += ' ';

            // unicode to bin

            bin_final_result += Number(decimal).toString(2);
            bin_final_result += ' ';


            // unicode to hex

            hex_final_result += Number(decimal).toString(16);
            hex_final_result += ' ';

        }

        try{
            decimal.value = final_result;
            h2.textContent = final_result;
        }
        catch (error){
            try{
                binary.value = bin_final_result;
                h2.textContent = bin_final_result;
            }
            catch (error){
                hex.value = hex_final_result.toUpperCase();
                h2.textContent = hex_final_result.toUpperCase();
            }
        }
        // unicode to bin

    });
}
catch (error){
    // do nothing 
}