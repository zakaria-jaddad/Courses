;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname student-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; student-starter.rkt

;; =================
;; Data definitions:

; 
; PROBLEM A:
; 
; Design a data definition to help a teacher organize their next field trip. 
; On the trip, lunch must be provided for all students. For each student, track 
; their name, their grade (from 1 to 12), and whether or not they have allergies.
; 


(define-struct student (name grade allergies?))
;; Student is (make-student String Natural[1, 12] Boolean)
;; Interp. a student with name, their grade from [1, 12] and true if alergic and false otherwise

;; Examples
(define S1 (make-student "Zakaria Jaddad" 2 true))
(define S2 (make-student "BabloByDo Chtaiba" 10 true)) ; If someone reading this GoodLuck
(define S3 (make-student "Zakaria Jaddad" 2 false))

;; Template
(define (fn-for-student student)
  (...
   (student-name student)      ; String
   (student-grade student)     ; Natural
   (student-allergies? student); Boolean
   )
  )

;; Template rules used
;; - compound 3 fields

;; =================
;; Functions:

; 
; PROBLEM B:
; 
; To plan for the field trip, if students are in grade 6 or below, the teacher 
; is responsible for keeping track of their allergies. If a student has allergies, 
; and is in a qualifying grade, their name should be added to a special list. 
; Design a function to produce true if a student name should be added to this list.
; 


;; Student -> Boolean
;; produce true if the student has allergies and is in a qualifying garde false otherwise

;; Stub
#;
(define (add-name? student) "")

;; Tests
(check-expect (add-name? S1) true)
(check-expect (add-name? S2) false)
(check-expect (add-name? S3) false)

;; Template
(define (add-name? student)
  (and (<= (student-grade student) 6) (student-allergies? student))
  )








