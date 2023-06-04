import { useState, useEffect } from "react";
import axios from "axios";
import styles from "./LoginUser.module.css";

const LoginUser = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const onSubmit = async (event) => {
    event.preventDefault();
    axios
      .post(
        "http://localhost:8000/user/rest-auth/login/",
        {
          email: email,
          password: password,
        },
        {
          headers: {
            "Content-Type": "application/json", // 요청 헤더에 JSON 형식으로 설정
          },
        }
      )
      .then(function (response) {
        // console.log(response);
        // localStorage.setItem("isLoggedIn", true);
        // window.location.reload();
        console.log(response);
        const token = response.data.key;
        localStorage.setItem("token", token);
        window.location.reload();
      })
      .catch(function (error) {
        console.log(error);
        console.log(error.response.data.non_field_errors[0]);
        setError((prev) => "로그인에 실패했습니다.");
      });
  };
  const onChange = (event) => {
    const { name, value } = event.target;
    if (name === "Email") {
      setEmail((prev) => value);
    } else if (name === "password") {
      setPassword((prev) => value);
    }
  };
  return (
    <div>
      {/* <h2 className={styles.title}>로그인</h2> */}
      <form onSubmit={onSubmit}>
        <input
          placeholder="Email"
          name="Email"
          value={email}
          onChange={onChange}
          required
        />
        <br />
        <input
          type="password"
          placeholder="비밀번호"
          name="password"
          value={password}
          onChange={onChange}
          required
        />
        <p>{error}</p>

        <hr />
        <input className={styles.submit} type="submit" value="로그인" />
      </form>
    </div>
  );
};
export default LoginUser;
