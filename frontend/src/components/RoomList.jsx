function List(props){
//     function Deleteroom(){
//   props.deletion(props.Roomno)
// }
    function checkIn(){
  props.checkin(props.Roomno)
}
    function checkOut(){
  props.checkout(props.Roomno)
}
    function reserve(){
  props.reserve(props.Roomno)
}
  return (
      <div className="room">
        <h1 >  Roomno: {props.Roomno} </h1>
        <p > RoomType: {props.RoomType}</p>
        <p > Status: {props.Status}</p>
        <p > Checkin: {props.Checkin}</p>
        <p > Reserved: { ''+props.Reserved}</p>
        {/* <button onClick={Deleteroom}>Delete</button> */}
        <button onClick={checkIn}>Checkin</button>
        <button onClick={checkOut}>Checkout</button>
        <button onClick={reserve}>Reserve</button>
      </div>
  )
}

export default List;