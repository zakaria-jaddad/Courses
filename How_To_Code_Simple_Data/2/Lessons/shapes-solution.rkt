;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname shapes-solution) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))


;; Polygon is one of:
;; - "triangle"
;; - "square"
;; - "pentagon"

;; Interp. type of plygons

;; <Examples are redundant for Enumeration>

#;
(define (fn-for-polugon polugon)
  (cond [(string=? polugon "triangle") (...)]
        [(string=? polugon "square") (...)]
        [(string=? polugon "pentagon") (...)])
  )
;; Templet rules used
;; - one of 3 case
;;  - atomic distinc: "triangle"
;;  - atomic distinc: "square"
;;  - atomic distinc: "pentagon"