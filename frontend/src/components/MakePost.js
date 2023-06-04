import { useState, useEffect } from "react";
import styles from "./MakePost.module.css"
import axios from "axios";
const MakePost = () => {
  const [title, setTitle] = useState("");
  const [context, setContext] = useState("");
  const [position, setPosition] = useState({ latitude: null, longitude: null });
  const [people, setPeople] = useState("");
  const [token, setToken] = useState("");
  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    setToken((prev) => storedToken);

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          setPosition({ latitude, longitude });
        },
        (error) => {
          console.error("Error getting geolocation:", error);
        }
      );
    } else {
      console.error("Geolocation is not supported by this browser.");
    }
  }, []);
  const onChange = (event) => {
    const { name, value } = event.target;
    if (name === "title") {
      setTitle((prev) => value);
    } else if (name === "context") {
      setContext((prev) => value);
    } else if (name === "people") {
      setPeople((prev) => value);
    }
  };
  //bring lat,lng from MapContainer
  // console.log(position);
  const onSubmit = async (event) => {
    event.preventDefault();
    await axios
      .post(
        "http://localhost:8000/api/",
        {
          title: title,
          content: context,
          lat: position.latitude,
          lng: position.longitude,
          personnel: people,
        },
        {
          headers: { Authorization: `Token ${token}` },
        }
      )
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    setTitle((prev) => "");
    setContext((prev) => "");
    setPeople((prev) => 0);
  };

  return (
    <div className={styles.container}>
      <div>
        <h2 className={styles.subTitle}>오늘밤 사냥을 나선다</h2>
      </div>
      <form className={styles.submitForm} onSubmit={onSubmit}>
        <input
          name="title"
          onChange={onChange}
          placeholder="제목"
          value={title}
          required
        />
        <br />
        <input
          name="context"
          onChange={onChange}
          placeholder="내용"
          value={context}
          required
        />
        <br />
        <input
          name="people"
          type="number"
          max="4"
          min="0"
          placeholder="인원"
          onChange={onChange}
          value={people}
          required
        />
        <br />
        <hr />
        <input className={styles.submitBtn} value="Submit" type="submit" />
      </form>
    </div>
  );
};
export default MakePost;
