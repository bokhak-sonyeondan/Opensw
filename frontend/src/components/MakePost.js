//수정 필요

import { useState } from "react";
import styles from './MakePost.module.css'
const MakePost = ({currentPosition}) => {
  const [title, setTitle] = useState("");
  const [context, setContext] = useState("");
  const [people, setPeople] = useState(0);
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
  console.log(currentPosition);
  const onSubmit = async (event) => {
    // event.preventDefault();
    await fetch("http://127.0.0.1:8000/api", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: title,
        content: context,
        people: people,
        //student id, people, department, phone number, lat, lng
      }),
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
    setTitle((prev) => "");
    setContext((prev) => "");
    setPeople((prev) => 0);
  };

  return (
    <div className={styles.makeform}>
      <form onSubmit={onSubmit}>
        <input
          name="title"
          onChange={onChange}
          placeholder="title"
          value={title}
          required
        />
        <br />
        <input
          name="context"
          onChange={onChange}
          placeholder="context"
          value={context}
          required
        />
        <br />
        <input
          name="people"
          type="number"
          max="4"
          min="0"
          onChange={onChange}
          value={people}
          required
        />
        <br />
        <input value="Submit" type="submit" />
      </form>
      <h2>{title}</h2>
    </div>
  );
};
export default MakePost;
