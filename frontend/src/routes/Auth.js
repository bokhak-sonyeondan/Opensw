import { useState } from "react";
import RegisterUser from "../components/auth/RegisterUser.js";
import LoginUser from "../components/auth/LoginUser.js";
import styles from "./Auth.module.css";
const Auth = ({ isLoggedIn,setIsLoggedIn }) => {
  const [first, setFirst] = useState(false);
  const onClick = () => {
    setFirst((prev) => !prev);
  };
  return (
    <div>
      <h1 className="title">CB💔U</h1>
      <div className={styles.context}>
        {first ? <RegisterUser /> : <LoginUser />}
        <button className={styles.toggle} onClick={onClick}>
          {first ? "로그인으로 이동" : "회원가입으로 이동"}
        </button>
      </div>
    </div>
  );
};

export default Auth;
