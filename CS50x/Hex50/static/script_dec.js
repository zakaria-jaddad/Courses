try{
    const decimal_input = document.getElementById('dec-input');

decimal_input.addEventListener('input', function(){
    try{
        if (Number(decimal_input.value)){
            let hex_final_result;
            let bin_final_result;
        
            let string = decimal_input.value;
        
            hex_final_result = Number(string).toString(16);
            
            // bin
            bin_final_result = Number(string).toString(2);
        
        
            try{
                hex.value = hex_final_result.toLocaleUpperCase();
                h2.textContent = hex_final_result.toUpperCase();
            }
            catch (error){
                binary.value = bin_final_result;
                h2.textContent = bin_final_result;
            }
        }
    }
    catch (error){
        // do nothing 
    }

});
}
catch (error){
    // do nothing 
}