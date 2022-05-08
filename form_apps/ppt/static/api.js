async function instructorCall(){
    let name = document.getElementById('id_instructor').value;
    console.log(name)
    let url = 'http://127.0.0.1:8000/getinstructor/' + name;
    const response = await fetch(url);
    let data = await response.json();
    console.log(data)

    let instructorName = document.querySelectorAll('.instructorName');
    for(let i = 0; i < instructorName.length; i++){
        instructorName[i].innerHTML = data.first_name + ' ' + data.last_name;
    }

    let signature = document.querySelectorAll('.instructorSignature');
    for(let i = 0; i < signature.length; i++){  
        signature.value = data.signature;
        // signature[i].src = "data:image/png;base64," + encoded ;
    }

    let reg = document.querySelectorAll('.instructorReg');
    for(let i = 0; i < reg.length; i++){
        reg[i].innerHTML = data.reg;
    }
}

async function instructor2Call(){
    let name = document.getElementById('id_instructor_2').value;
    let url = 'http://127.0.0.1:8000/getinstructor/' + name;
    const response = await fetch(url);
    let data = await response.json();

    let instructorName = document.querySelectorAll('.instructor2Name');
    for(let i = 0; i < instructorName.length; i++){
        instructorName[i].innerHTML = data.name;
    }

    let signature = document.querySelectorAll('.instructor2Signature');
    for(let i = 0; i < signature.length; i++){
        signature[i].src = data.signature;
    }

    let reg = document.querySelectorAll('.instructor2Reg');
    for(let i = 0; i < reg.length; i++){
        reg[i].innerHTML = data.reg;
    }
}


async function get_customer(){
    let name = document.getElementById('id_company_Name').value;
    let url = 'http://127.0.0.1:8000/getcustomer/' + name;
    const response = await fetch(url);
    let data = await response.json();

    let companyName = document.querySelectorAll('.company_name')
    for(let i = 0; i < companyName.length; i++){
        companyName[i].value = data.company_name;
    }

    let contact = document.querySelectorAll('.company_contact')
    for(let i = 0; i < contact.length; i++){
        contact[i].value = data.company_contact;
    }

    let address = document.querySelectorAll('.company_address')
    for(let i = 0; i < address.length; i++){
        address[i].value = data.company_address;
    }
}