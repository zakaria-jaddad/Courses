;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname tuition) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; tuition-graph-starter.rkt  (just the problem statements)
;; tuition-graph-v1.rkt       (includes constants)

; 
; PROBLEM:
; 
; Eva is trying to decide where to go to university. One important factor for her is 
; tuition costs. Eva is a visual thinker, and has taken Systematic Program Design, 
; so she decides to design a program that will help her visualize the costs at 
; different schools. She decides to start simply, knowing she can revise her design
; later.
; 
; The information she has so far is the names of some schools as well as their 
; international student tuition costs. She would like to be able to represent that
; information in bar charts like this one:
; 
; 
;         .
;         
; (A) Design data definitions to represent the information Eva has.
; (B) Design a function that consumes information about schools and their
;     tuition and produces a bar chart.
; (C) Design a function that consumes information about schools and produces
;     the school with the lowest international student tuition.
; 



;; Constants:

(define FONT-SIZE 24)
(define FONT-COLOR "black")

(define Y-SCALE   1/200)
(define BAR-WIDTH 30)
(define BAR-COLOR "lightblue")


;; Data definitions:

(define-struct school (name tuition))
;; School is (make-school String Natural)
;; Interp. name is the school name, tuition is INTERNATIONAL STUDENT'S TUITIONS in USD

(define S1 (make-school "School1" 27797))
(define S2 (make-school "School2" 23300))
(define S3 (make-school "School3" 20042))

(define (fn-for-school s)
  (... (school-name s)
       (school-tuition s)))

;; Template rules used:
;;   - compound: (make-school String Natural)

;; ListOfSchool is one of:
;;   - empty
;;   - (cons School ListOfSchool)
;; Interp. a list of schools
(define LOS1 empty)
(define LOS2 (cons S1 (cons S2 (cons S3 empty))))

(define (fn-for-los los)
  (cond [(empty? los) (...)]
        [else
         (... (fn-for-school (first los))
             (fn-for-los (rest los)))]
  ))

;; Template rules used:
;; - one of: 2 cases
;; - atomic distinc: empty
;; - compound: (cons School ListOfSchool)
;; - reference: (first los)
;; - slef-reference: (rest los) is ListOfSchool

;; Functions:

;; ListOfSchool -> Image
;; prduce bar chart showing names and tuitions of each school in list
(check-expect (chart empty) (square 0 "solid" "white"))
(check-expect (chart (cons (make-school "s1" 8000) empty))
                           (beside/align "bottom"
                                         (draw-school(make-school "s1" 8000))
                                         (square 0 "solid" "white")))
                           

;(define (chart los) (square 0 "solid" "white")) ;stub

(define (chart los)
  (cond [(empty? los) (square 0 "solid" "white")]
        [else
         (beside/align "bottom"
                       (draw-school (first los))
                       (chart (rest los)))]
  ))

;; School -> Image
;; produce school chart
(check-expect (draw-school (make-school "s1" 8000))
              (overlay/align "center" "bottom"
                             (rotate -90 (text "s1" FONT-SIZE FONT-COLOR))
                             (rectangle BAR-WIDTH (* Y-SCALE 8000) "solid" BAR-COLOR))
              )
;(define (draw-school s) (square 0 "solid" "white")) ;stub
(define (draw-school s)
  (overlay/align "center" "bottom"
                 (rotate -90 (text (school-name s) FONT-SIZE FONT-COLOR))
                 (rectangle BAR-WIDTH (* Y-SCALE (school-tuition s)) "solid" BAR-COLOR))
  )


;;
(define los (cons S1 (cons S2 (cons S3 empty))))
(chart los)




