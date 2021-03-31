import React, { useState, useEffect } from "react";
import { getCourses } from "../api/courseApi";
import CourseList from "./CourseList";
import { Link } from "react-router-dom";

function CoursesPage() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    getCourses().then(_courses => setCourses(_courses));
  }, []);

  return (
    <>
    <div className="navbar navbar-light bg-dark">
      <Link className="btn btn-outline-warning" to="/course">Add Course</Link>
      <Link className="btn btn-outline-warning" to="/course">Actions</Link>
    </div>
    <br></br>
    <br></br>
    <CourseList courses={courses} />
    </>
  );
}

export default CoursesPage;
