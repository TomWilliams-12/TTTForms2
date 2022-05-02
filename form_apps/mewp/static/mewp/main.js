// Automate Candidate name inputs from
function updateCandidateName(){
    let candidateName = document.querySelector('#id_candidate_Name').value;
    let nameSpaces = document.querySelectorAll('.candidate_Name');

    for(let i = 0; i < nameSpaces.length; i++) {
        nameSpaces[i].value = candidateName;
    }
}

//Automate the initals on induction page
function initialAll(){
    let initials = document.querySelectorAll('.initials');
    let value = document.querySelector('#id_candidate_Initial').value;

    for (let i = 0; i < initials.length; i++){
        initials[i].value = value
    }
}

//Automate the TOPS ID input across the form
function updateTopsID(){
    let topsID = document.querySelectorAll('.tops_ID');
    let value = document.querySelector('#id_candidateTopsId').value;

    for (let i = 0; i < topsID.length; i++){
        topsID[i].value = value
    }
}


//Automate the start and end dates across the form 
function startDateAutofill(){
    let startDate = document.querySelector('#id_start_Date').value;
    let startDateAutofill = document.querySelectorAll('.start_Date');

    for(let i = 0; i < startDateAutofill.length; i++){
        startDateAutofill[i].value = startDate;
    }
}

function endDateAutofill(){
    let endDate = document.querySelector('#id_finish_Date').value;
    let endDateAutofill = document.querySelectorAll('.end_Date');

    for(let i = 0; i < endDateAutofill.length; i++){
        endDateAutofill[i].value = endDate;
    }
}

// Autofill the venue
function venueAutofill(){
    let venue = document.getElementById('id_venue').value;
    let venueAutofill = document.querySelectorAll('.venueAutofill');
    for (let i = 0; i < venueAutofill.length; i++){
        venueAutofill[i].value = venue;
    }
}


//Calculate the percentage for the Theory Test
let marks = document.querySelectorAll('.atMark');
let percent = document.querySelectorAll('.percentageCalculator');
let totalMarks = 0
for(let i = 0; i < marks.length; i++){
    let currentValue = parseInt(marks[i].value);
    totalMarks += currentValue;

    marks[i].addEventListener('change', function () {
        let newValue = parseInt(marks[i].value);
        totalMarks -= currentValue;
        totalMarks += newValue;
        currentValue = newValue;
        for (let i = 0; i < percent.length; i ++){
            percent[i].innerHTML = totalMarks + '%';
        }
    })
}
// This function is to call on page load for existing forms
function percentageCalculator() {
    let marks = document.querySelectorAll('.atMark');
    let percent = document.querySelectorAll('.percentageCalculator');
    let totalMarks = 0

    for (let i = 0; i < marks.length; i++) {
        let x = parseInt(marks[i].value);
        totalMarks += x;
        for (let i = 0; i < percent.length; i++) {
                percent[i].innerHTML = totalMarks + '%';
            }
    }
}

// Calculate the test duration
function calculateDuration(){
    let start = document.getElementById('id_start_Time').value;
    let stop = document.getElementById('id_finish_Time').value;
    let set = document.getElementById('id_set_Time').value;
        if (!start || !stop) return;
        let startTime = "2021-05-09 " + start + ":00";
        let endTime = "2021-05-09 " + stop + ":00";
        let startArr = startTime.split(/[- :T]/);
        let finishArr = endTime.split(/[- :T]/);
        let startVal = new Date(startArr[0], startArr[1]-1, startArr[2], startArr[3], startArr[4], startArr[5]);
        let stopVal = new Date(finishArr[0], finishArr[1]-1, finishArr[2], finishArr[3], finishArr[4], finishArr[5]);
        // set = set.split("m");
        let dur = stopVal-startVal;
        let seconds = Math.floor(dur/1000);
        let minutes = Math.floor(seconds / 60);
        let setTime = parseInt(set[0]);
        let excess = minutes - set;
        if (excess <= 0){
            excess = 0;
        }
        document.getElementById('duration').innerHTML = minutes + "m";
        document.getElementById('excessTime').innerHTML = excess + "m";
        updateTimePenalties(excess);
}

// Functions and Variables to calculate the penalty points on practical test
let plusBtns = document.querySelectorAll('.plusBtn');
let minusBtns = document.querySelectorAll('.minusBtn');
let fault = document.querySelectorAll('.faults');
let award = document.querySelectorAll('.award');
let penalty = document.querySelectorAll('.penalty');
let pen1 = document.querySelectorAll('.pen1');
let cft = document.getElementById('carryForwardTotal');
let tp = document.getElementById('totalPenalties');
let tpc = document.getElementById('totalPenaltiesCopy');
let awardTotal = 0;
let forwardTotal = 0;
let totalPenalties = 0;
let carryForwardDyn = document.querySelector('#carryForwardDyn').innerHTML;


for(let i = 0; i < plusBtns.length; i++) {
    plusBtns[i].addEventListener('click', function () {
        fault[i].innerHTML += 'x ';
        awardTotal = parseInt(penalty[i].innerHTML) * (fault[i].innerHTML.length / 2);
        award[i].value = awardTotal;

        if (i < carryForwardDyn) {
            forwardTotal += parseInt(pen1[i].innerHTML);
            cft.innerHTML = forwardTotal;
        }
        updateTotalPenalties('+', i);
    })

    minusBtns[i].addEventListener('click', function () {
        if( award[i].value <= 0){

        } else {
            fault[i].innerHTML = fault[i].innerHTML.slice(0, -1);
            fault[i].innerHTML = fault[i].innerHTML.slice(0, -1);
            awardTotal = parseInt(penalty[i].innerHTML) * (fault[i].innerHTML.length / 2);
            award[i].value = awardTotal;
            if (i < carryForwardDyn) {
                forwardTotal -= parseInt(penalty[i].innerHTML);
                cft.innerHTML = forwardTotal;
        }
        updateTotalPenalties('-', i);
        }

    })
}

function updateTimePenalties(excess){
    if (excess <= 0){
        document.getElementById('timePenalties').innerHTML = '0';
        updateTotalPenalties('time', 0);
    } else {
        document.getElementById('timePenalties').innerHTML = excess + '';
        updateTotalPenalties('time', excess);
    }
}

function updateTotalPenalties(mod, i){
        if(mod === '-') {
            totalPenalties -= parseInt(penalty[i].innerHTML);
            let excess = getExcess();
            tp.innerHTML = totalPenalties + excess;
            tpc.innerHTML = totalPenalties + excess;
            if (parseInt(tp.innerHTML) <= 0) {
                totalPenalties = 0;
                tp.innerHTML = totalPenalties + excess;
                tpc.innerHTML = totalPenalties + excess;
            }
        } else if (mod === '+'){
            totalPenalties += parseInt(penalty[i].innerHTML);
            let excess = getExcess();
            tp.innerHTML = totalPenalties + excess;
            tpc.innerHTML = totalPenalties + excess;
        } else if(mod === 'time'){
            tp.innerHTML = totalPenalties + i;
            tpc.innerHTML = totalPenalties + i;
        }
    }

    function onLoadUpdateTotalPenalties(){
    let award = document.querySelectorAll('.award');
    let excess = getExcess();
    for(let i = 0; i < award.length; i++) {
        if(award[i].value == ''){
           award[i].value = 0;
        }
        totalPenalties += parseInt(award[i].value);
    }
    tp.innerHTML = parseInt(totalPenalties) + excess;
    tpc.innerHTML = parseInt(totalPenalties) + excess;
}


function getExcess(){
    let excess = document.getElementById('excessTime').innerHTML;
    if(excess === ''){
        return 0;
    } else {
        return parseInt(excess);
    }
}

// SHOW/HIDE INSTRUCTOR SIGNATURE
function instructorSign(){
    let instructorSig = document.querySelectorAll('.instructorSigs');
    let candidateSig = document.querySelectorAll('.candidateSigs');
    let sigDate = document.querySelectorAll('.sigDate');

    for(let i =0; i < instructorSig.length; i++){
        if (sigDate[i].value){
            instructorSig[i].classList.remove('d-none');
            candidateSig[i].classList.remove('d-none');
        }
        else {
            instructorSig[i].classList.add('d-none');
            candidateSig[i].classList.add('d-none');
        }
    }
}


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
        contact[i].value = data.company_contact_first_name + ' ' + data.company_contact_last_name;
    }

    let address = document.querySelectorAll('.company_address')
    for(let i = 0; i < address.length; i++){
        address[i].value = data.company_address_line_1;
    }
}

function capacityAutofill(){
    let capacity = document.querySelector('.capacity').value;
    let capacityFill = document.querySelectorAll('.capacityFill');

    for (let i = 0; i < capacityFill.length; i++){
        capacityFill[i].value = capacity;
    }
}

function liftHeightAutofill() {
    let testHeight = document.querySelector('.testHeight').value;
    let testHeightFill = document.querySelectorAll('.testHeightFill');

    for (let i = 0; i < testHeightFill.length; i++){
        testHeightFill[i].value = testHeight;
    }
}

function motiveAutofill(){
    let motive = document.querySelector('.motive').value;
    let motiveAutofill = document.querySelectorAll('.motiveAuto');
    for (let i = 0; i < motiveAutofill.length; i++){
        motiveAutofill[i].value = motive;
    }
}

function updateTruck(){
    let truckType = document.querySelector('.truckType').value;
    let truckFill = document.querySelectorAll('.truckFill');

    for (let i = 0; i < truckFill.length; i++) {
        truckFill[i].value = truckType;
    }
}
function updateModel(){
    let modelType = document.querySelector('.truckModel').value;
    let modelFill = document.querySelectorAll('.modelFill');

    for (let i = 0; i < modelFill.length; i++) {
        modelFill[i].value = modelType;
    }
}


function onload(){
    startDateAutofill();
    endDateAutofill();
    initialAll();
    updateTopsID();
    updateCandidateName();
    onLoadUpdateTotalPenalties();
    venueAutofill();
    calculateDuration();
    instructorSign();
    percentageCalculator();
    capacityAutofill();
    liftHeightAutofill();
    motiveAutofill();
    updateModel();
    updateTruck();
}
