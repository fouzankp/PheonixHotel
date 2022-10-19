function List(props){
    function handleClick(){
  props.deletion(props.Roomno)
}
  return (
      <div className="room">
        <h1 >  Roomno: {props.Roomno} </h1>
        <p > RoomType: {props.RoomType}</p>
        <p > Status: {props.Status}</p>
        <p > Checkin: {props.Checkin}</p>
        <p > Reserved: {props.Reserved}</p>
        <button onClick={handleClick}>Delete</button>
      </div>
  )
}

export default List;