import {useState, useEffect} from "react"
import axios from "axios"
import List from "./RoomList"

function Room() {
    const [rooms, setNewRooms] = useState(null)
    const [formRoom, setFormRoom] = useState({
        Roomno: 0,
        RoomType: "S",
        Status: "C",
        Checkin: null,
        Reserved: false
    })

    useEffect(() => {
        getRooms()
          } ,[])

    function getRooms() {
    axios({
        method: "GET",
        url:"/rooms/",
      }).then((response)=>{
        const data = response.data
        setNewRooms(data)
      }).catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
          }
      })}

      function createRoom(event) {
        axios({
          method: "POST",
          url:"/rooms/",
          data:{
            Roomno: formRoom.Roomno,
            RoomType: formRoom.RoomType,
            Status: formRoom.Status,
            Checkin: formRoom.Checkin,
            Reserved: formRoom.Reserved
           }
        })
        .then((response) => {
          getRooms()
        })
    
        setFormRoom(({
          Roomno: 0,
          RoomType: "S",
          Status: "C",
          Checkin: null,
          Reserved: false}))
    
        event.preventDefault()
    }

    function DeleteRoom(id) {
        axios({
          method: "DELETE",
          url:`/rooms/${id}`,
        })
        .then((response) => {
          getRooms()
        });
    }

    function handleChange(event) { 
        const {value, name} = event.target
        setFormRoom(prevRoom => ({
            ...prevRoom, [name]: value})
        )}

    return (
    <div className=''>

      <form className="create-note">
          <input onChange={handleChange} text={formRoom.Roomno} name="Roomno" placeholder="Roomno" value={formRoom.Roomno} />
          <input onChange={handleChange} text={formRoom.RoomType} name="RoomType" placeholder="RoomType" value={formRoom.RoomType} />
          <input onChange={handleChange} text={formRoom.Status} name="Status" placeholder="Status" value={formRoom.Status} />
          <input type="date" onChange={handleChange} text={formRoom.Checkin} name="Checkin" placeholder="Checkin" value={formRoom.Checkin} />
          <input onChange={handleChange} text={formRoom.Reserved} name="Reserved" placeholder="Reserved" value={formRoom.Reserved} />
          <button onClick={createRoom}>Create Room</button>
      </form>
          { rooms && rooms.map(room => <List
          key={room.Roomno}
          Roomno={room.Roomno}
          RoomType={room.RoomType}
          Status={room.Status} 
          Checkin={room.Checkin} 
          Reserved={room.Reserved} 
          deletion ={DeleteRoom}
          />
          )}

    </div>
  );
          
}

export default Room
