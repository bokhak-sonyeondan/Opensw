import { useState } from "react";
import axios from "axios";
import styles from "./RegisterUser.module.css";
const RegisterUser = () => {
  const [email, setEmail] = useState("");
  const [ps1, setPs1] = useState("");
  const [ps2, setPs2] = useState("");
  const [age, setAge] = useState("");
  const [gender, setGender] = useState("");
  const [phone, setPhone] = useState("");
  const [major, setMajor] = useState("");
  const [real, setReal] = useState("");
  const [error, setError] = useState("");
  const [isSuccess,setIsSuccess]=useState(true);
  const onChange = (event) => {
    const { name, value } = event.target;
    if (name === "Email") {
      setEmail((prev) => value);
    } else if (name === "Password1") {
      setPs1((prev) => value);
    } else if (name === "Password2") {
      setPs2((prev) => value);
    } else if (name === "Age") {
      setAge((prev) => value);
    } else if (name === "Gender") {
      setGender((prev) => value);
    } else if (name === "Phone") {
      setPhone((prev) => value);
    } else if (name === "Major") {
      setMajor((prev) => value);
    } else if (name === "Realname") {
      setReal((prev) => value);
    }
  };
  const onSubmit = (event) => {
    event.preventDefault();
    axios
      .post(
        "http://127.0.0.1:8000/user/rest-auth/registration/",
        {
          email: email,
          password1: ps1,
          password2: ps2,
          age: age,
          gender: gender,
          phone: phone,
          major: major,
          realname: real,
        },
        {
          headers: {
            "Content-Type": "application/json", // 요청 헤더에 JSON 형식으로 설정
          },
        }
      )
      .then(function (response) {
        console.log(response);
        // localStorage.setItem("isLoggedIn", true);
        // window.location.reload();
        setIsSuccess(true);
        setError((prev)=>"이메일이 전송되었습니다.");
      })
      .catch(function (error) {
        console.log(error);
        setIsSuccess(false);
        setError((prev)=>"회원가입에 실패했습니다.")
      });
  };

  return (
    <div className={styles.container}>
      {/* <h2 className={styles.title}>회원가입</h2> */}
      <form onSubmit={onSubmit}>
        <input
          name="Email"
          onChange={onChange}
          placeholder="충북대 웹메일"
          value={email}
          required
        />
        <br />
        <input
          name="Password1"
          onChange={onChange}
          placeholder="비밀번호"
          value={ps1}
          type="password"
          required
        />
        <br />
        <input
          name="Password2"
          onChange={onChange}
          placeholder="비밀번호 재입력"
          value={ps2}
          type="password"
          required
        />
        <br />
        <input
          name="Age"
          onChange={onChange}
          placeholder="나이"
          value={age}
          min="0"
          max="100"
          type="number"
          required
        />
        <br />

        <input
          name="Phone"
          onChange={onChange}
          placeholder="전화번호"
          value={phone}
          type="tel"
          required
        />
        <br />
        <input
          name="Major"
          onChange={onChange}
          placeholder="전공"
          value={major}
          required
        />
        <br />
        <input
          name="Realname"
          onChange={onChange}
          placeholder="이름"
          value={real}
          required
          id="name"
        />
        <br />
        <div className={styles.radio}>
          <input
            onChange={onChange}
            checked={gender === "M"}
            className={styles.radio}
            type="radio"
            id="genderChoice1"
            name="Gender"
            value="M"
          />
          <label htmlFor="genderChoice1">남성</label>
          <input
            onChange={onChange}
            className={styles.radio}
            checked={gender === "F"}
            type="radio"
            id="genderChoice2"
            name="Gender"
            value="F"
          />
          <label htmlFor="genderChoice2">여성</label>
        </div>
        <p className={isSuccess?styles.success:styles.error}>{error}</p>
        <hr/>
        <input className={styles.submit} type="submit" value="회원가입" />
      </form>
    </div>
  );
};
export default RegisterUser;
