
function runPythonScript()
{
    console.log('test')
    //spawner = require('child_process').spawn;
    //const datatopass = 'send this to python script';
    //const process = spawner('python',['./db_to_python.py',datatopass])
    //process.stdout.on('data', data =>{
    //console.log('data ==',data.toString())
   // })
}

function SetUtilisateur() {
    nom= document.getElementById("nom").value
    prenon= document.getElementById("prenom").value
    email= document.getElementById("email").value
    telephone= document.getElementById("telephone").value
    mdp= document.getElementById("mdp").value
    //console.log('test')
    runPythonScript()
}
runPythonScript()