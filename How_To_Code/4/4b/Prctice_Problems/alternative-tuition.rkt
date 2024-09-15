;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname alternative-tuition) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
;; alternative-tuition-graph-starter.rkt

; 
; Consider the following alternative type comment for Eva's school tuition 
; information program. Note that this is just a single type, with no reference, 
; but it captures all the same information as the two types solution in the 
; videos.
; 
; (define-struct school (name tuition next))
; ;; School is one of:
; ;;  - false
; ;;  - (make-school String Natural School)
; ;; interp. an arbitrary number of schools, where for each school we have its
; ;;         name and its tuition in USD
; 
; (A) Confirm for yourself that this is a well-formed self-referential data 
;     definition.
; 
; ;; ok this well formed is this what he want? :|
; ;; the last school should have a name, tuition and next must be empty
; 
; 
; (B) Complete the data definition making sure to define all the same examples as 
;     for ListOfSchool in the videos.
; 
; (C) Design the chart function that consumes School. Save yourself time by 
;     simply copying the tests over from the original version of chart.
; 
; (D) Compare the two versions of chart. Which do you prefer? Why?
; 


;; Constants:

(define FONT-SIZE 24)
(define FONT-COLOR "black")

(define Y-SCALE   1/200)
(define BAR-WIDTH 30)
(define BAR-COLOR "lightblue")

;; =========
;; Data Definition

(define-struct school (name tuition next))
;; School is one of:
;;  - false
;;  - (make-school String Natural School)
;; interp. an arbitrary number of schools, where for each school we have its
;;         name and its tuition in USD

(define S3 (make-school "School3" 20042 empty))
(define S2 (make-school "School2" 17795 S3))
(define S1 (make-school "School1" 27790 S2))

#;
(define (fn-for-school s)
  (cond
    [(empty? (school-next s)) (...)]
        [else
         (... (... (make-school (school-name s) (school-tuition s)))
              (fn-for-los next))
         ]
        ))

;; Templet rules used
;;  - compound (make-school String Natural School)
;; IDK 


;; Functions:

;; ListOfSchool -> Image
;; prduce bar chart showing names and tuitions of each school in list
(check-expect (chart (make-school "s1" 8000 empty))
              (beside/align "bottom"
                            (draw-school(make-school "s1" 8000 empty))
                            (square 0 "solid" "white")))
                           

;(define (chart los) (square 0 "solid" "white")) ;stub

(define (chart s)
  (cond [(empty? (school-next s))
         (beside/align "bottom"
                       (draw-school s)
                       (square 0 "solid" "white"))
         ]
        [else
         (beside/align "bottom"
                       (draw-school s)
                       (chart (school-next s)))
         ]))

;; School -> Image
;; produce school chart
(check-expect (draw-school (make-school "s1" 8000 empty))
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

(chart S1)
;; Khouna wlahta mride Fkarou!