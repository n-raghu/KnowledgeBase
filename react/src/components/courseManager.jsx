import React, { useEffect, useState } from "react";
import CourseForm from "./CourseForm";
import * as courseAPI from "../api/courseApi";
import {toast} from "react-toastify";

const ManageCoursePage = props => {
    const [errors, setErrors] = useState({});
    const [course, setCourse] = useState({
        id: null,
        slug: "",
        title: "",
        authorId: "",
        category: ""
    });

    useEffect(() => {
        const slug = props.match.params.slug;
        if (slug) {
            courseAPI.getCourseBySlug(slug).then(_course => setCourse(_course));
        }
    }, [props.match.params.slug]);

    function handleChange({ target }) {
        setCourse({
            ...course,
            [target.name]: target.value
        });
    }

    function formIsValid() {
        const _errors = {};

        if (!course.title) _errors.title = "Title is required";
        if (!course.authorId) _errors.authorId = "Author ID is required";
        if (!course.category) _errors.category = "Category is required";
        
        setErrors(_errors)
        return Object.keys(_errors).length === 0;
    }

    function eventSubmit(event) {
        event.preventDefault();
        if (!formIsValid()) return;
        courseAPI.saveCourse(course).then(() => {
            props.history.push("/courses");
            toast.success("Course saved.");
        });
    }

    function eventCancel() {
        console.log("Cancel call");
        //props.history.push("/courses");
        //toast.cancel("Changes Ignored.")
    }

    return (
        <>
            <h2>Modify Course</h2>
            <CourseForm
                errors={errors}
                course={course}
                onChange={handleChange}
                onSubmit={eventSubmit}
                onCancel={eventCancel}
            />
        </>
    );

};

export default ManageCoursePage;
