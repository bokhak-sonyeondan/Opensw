import KakaoMap from "../components/KakaoMap";
import styles from "./Home.module.css";
import MakePost from "../components/MakePost";
import { useState } from "react";

const Home = () => {
  const [form, setForm] = useState(false);
  const toggle = () => {
    setForm((prev) => !prev);
  };
  const logout = () => {
    localStorage.removeItem("token");
    window.location.reload();
  };
  return (
    <div>
      <h1>Home</h1>
      <KakaoMap />
      <span className={styles.logout} onClick={logout}>
        로그아웃
      </span>
      {form ? (
        <>
          <span className={styles.submitBtn} onClick={toggle}>
            인연찾기
          </span>
          <MakePost />
        </>
      ) : (
        <span className={styles.submitBtn} onClick={toggle}>
          인연찾기
        </span>
      )}
      {/* <MakePost /> */}
    </div>
  );
};

export default Home;
