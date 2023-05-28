import { useState, useEffect } from 'react';
import './App.css';


// fetches the Data from server.  
const GenerateSensorData = ({setList}) => {
  useEffect (() => {
    async function fetchSensors () {
      const response = await fetch("http://olivier.lan:4000/senseurs")
      const listeJsonSensor = await response.json()
      let mocklist = []
      listeJsonSensor.forEach(sensor => {
        sensor = {...sensor, isActive:true};
        mocklist = [...mocklist, sensor];
      });
      setList(mocklist)
    }
    fetchSensors();
  },[])
}

const Header = ({maxNoise, maxHumidity, maxTemp, list, activeCounter}) => {

  let avgTemp = 0; let avgHumidity = 0; let avgNoise = 0 ; 
  list.forEach(element => {
    if (element.isActive) {
      avgTemp += element.temperature ; avgHumidity += element.humidite ; avgNoise += element.niveauBruit
    }
  });

  avgTemp = avgTemp / activeCounter ; avgHumidity = avgHumidity / activeCounter ; avgNoise = avgNoise / activeCounter ; 
  return (

    <div className='row m-2'>
      <div className='col-md-6'>
        <h1>Valeur moyennes</h1>
        <h2>{avgTemp.toFixed(2)} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C</h2>
        <h2>{avgHumidity.toFixed(2)} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;% hum</h2>
        <h2>{avgNoise.toFixed(2)} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dB</h2>
      </div>
      <div className='col-md-6'>
        <h1>Maximums</h1>
        <h2>{maxTemp} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C</h2>
        <h2>{maxHumidity} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;% hum</h2>
        <h2>{maxNoise} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dB</h2>
      </div>
    </div>
  );

}

const Sensor = ({sensor,  setClicked, list, methodToSet }) => {

  let maxTemp = 0; let maxhumidity = 0; let maxNoise = 0;
  list.forEach(loopSensor => {
    if (loopSensor.isActive === true && loopSensor.temperature > maxTemp) { maxTemp = loopSensor.temperature}
    if (loopSensor.isActive === true && loopSensor.humidite > maxhumidity) { maxhumidity = loopSensor.humidite}
    if (loopSensor.isActive === true && loopSensor.niveauBruit > maxNoise) { maxNoise = loopSensor.niveauBruit}
  })

  let maxTempId = null; let maxHumidityId = null; let maxNoiseId = null
  list.forEach(element => {
    if (maxTemp === element.temperature) {maxTempId = element.idSenseur}
    if (maxhumidity === element.humidite) {maxHumidityId = element.idSenseur}
    if (maxNoise === element.niveauBruit) {maxNoiseId = element.idSenseur}
  });
  
  // defining yellow text classes
  // temp
  let maxTempclass = ""
  if (sensor.isActive) {
    maxTempclass = maxTempId === sensor.idSenseur ? "card-title text-warning" : "card-title" 
  } else { maxTempclass =  "card-title text-secondary"}
  // humidity
  let maxHumidityClass = ""
  if (sensor.isActive) {
    maxHumidityClass = maxHumidityId === sensor.idSenseur ? "card-title text-warning" : "card-title" 
  } else { maxHumidityClass =  "card-title text-secondary"}
  
  // Noise
  let maxNoiseClass = ""
  if (sensor.isActive) {
    maxNoiseClass = maxNoiseId === sensor.idSenseur ? "card-title text-warning" : "card-title" 
  } else { maxNoiseClass =  "card-title text-secondary"}

  let setMaxTemp = methodToSet("t") ; let setMaxHumidity = methodToSet("h") ; let setMaxNoise = methodToSet("n") ;
  setMaxTemp(maxTemp) ; setMaxHumidity(maxhumidity) ; setMaxNoise(maxNoise)

  let status = sensor.isActive

  return (
    <div className={status?"card col-sm m-1 text-bg-primary":"card col-sm m-1 border-primary"}>
        <h5 className="card-header">{sensor.lieu}</h5>
        <div className="card-body">
          <h5 className={maxTempclass}>{sensor.temperature} C</h5>
          <h5 className={maxHumidityClass}>{sensor.humidite} % hum</h5>
          <h5 className={maxNoiseClass}>{sensor.niveauBruit} dB</h5>
          <h6>{sensor.concentrationCO2} ppm CO2</h6>
          <h6>{sensor.luminosite} lx</h6>
          <button id={sensor.idSenseur} className={status?'btn btn-light':"btn btn-outline-primary"} onClick={()=>setClicked(sensor.idSenseur-1)}>Désactiver</button>
        </div>
    </div>
  );

}

const App = () => {

  const [jsonSensorDataActive, setSensorData] = useState(null);
  const [buttonClicked, setClickedButton] = useState(null);
  const [numActiveButtons, setNumActiveButtons] = useState(6);
  const [maxTemp, setTemp] = useState(0); 
  const [maxHumidity, setHumidity] = useState(0); 
  const [maxNoise, setMaxNoise] = useState(0); 
  

  const whichSet = (operand) => {
    if (operand === "t") {return setTemp}
    else if (operand === "h") {return setHumidity}
    else if (operand === "n") {return setMaxNoise}
    else {console.log("error in whichset method");}
  }

  useEffect(()=>{
    if (buttonClicked !== null) {
      if (numActiveButtons === 1 && jsonSensorDataActive[buttonClicked].isActive === true ) {
        console.log("woopwoop");

      } else {

        jsonSensorDataActive[buttonClicked].isActive ? setNumActiveButtons(numActiveButtons - 1) : setNumActiveButtons(numActiveButtons + 1) 

        jsonSensorDataActive[buttonClicked].isActive = !jsonSensorDataActive[buttonClicked].isActive 
        setClickedButton(null)
        console.log(jsonSensorDataActive);
      }
    }
  },[buttonClicked]);

  
  

  return (
    <div className='container p-3'>
      <GenerateSensorData setList={setSensorData}  />
   
      
      {/* First row */}
      { jsonSensorDataActive && <Header maxHumidity={maxHumidity} maxTemp={maxTemp} maxNoise={maxNoise} list={jsonSensorDataActive} activeCounter = {numActiveButtons}/>}

      {/* Second row */}
      <div className='row'>
      { jsonSensorDataActive && <Sensor sensor={jsonSensorDataActive[0]} setClicked={setClickedButton} list={jsonSensorDataActive} methodToSet={whichSet}/> }
      { jsonSensorDataActive && <Sensor sensor={jsonSensorDataActive[1]} setClicked={setClickedButton} list={jsonSensorDataActive} methodToSet={whichSet}/> }
      { jsonSensorDataActive && <Sensor sensor={jsonSensorDataActive[2]} setClicked={setClickedButton} list={jsonSensorDataActive} methodToSet={whichSet}/> }
      </div>
      
	    {/* Third row */}
        <div className='row'>
        { jsonSensorDataActive && <Sensor sensor={jsonSensorDataActive[3]} setClicked={setClickedButton} list={jsonSensorDataActive} methodToSet={whichSet}/> }
        { jsonSensorDataActive && <Sensor sensor={jsonSensorDataActive[4]} setClicked={setClickedButton} list={jsonSensorDataActive} methodToSet={whichSet}/> }
        { jsonSensorDataActive && <Sensor sensor={jsonSensorDataActive[5]} setClicked={setClickedButton} list={jsonSensorDataActive} methodToSet={whichSet}/> }
        </div>
      </div>

  );
}

export default App;