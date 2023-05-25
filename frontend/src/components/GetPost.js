import { useState, useEffect } from "react";
import axios from "axios";
const GetPost = () => {
  const [title, setTitle] = useState([]);

  useEffect(()=>{
    axios.get('http://127.0.0.1:8000/api/')
  .then(function (response) {
    // 성공 핸들링
    console.log(response);
  })
  .catch(function (error) {
    // 에러 핸들링
    console.log(error);
  })
  .finally(function () {
    // 항상 실행되는 영역
  });
  },[])
  return <div></div>;
};
export default GetPost;
