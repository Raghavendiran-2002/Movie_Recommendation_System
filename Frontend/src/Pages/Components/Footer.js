// Footer Component
import "./styles/Footer.css";
import React from "react";
const Footer = () => {
  return (
    <footer>
      <div className="footer">
        <div id="row1" className="row ">
          <a
            href="https://www.linkedin.com/in/"
            target="_blank"
            rel="noreferrer"
          >
            <i className="fa fa-linkedin"></i>
          </a>
          <a
            href="https://github.com/Raghavendiran-2002/"
            target="_blank"
            rel="noreferrer"
          >
            <i className="fa-brands fa-github"></i>
          </a>
          <a
            href="https://www.instagram.com/_raghavendiran_/"
            target="_blank"
            rel="noreferrer"
          >
            <i className="fa fa-instagram"></i>
          </a>
        </div>
        <div id="row1" className="row">
          © Developed By Raghavendiran N
        </div>
      </div>
    </footer>
  );
};

export default Footer;
