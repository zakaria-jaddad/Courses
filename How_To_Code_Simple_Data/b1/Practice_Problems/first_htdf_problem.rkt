;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname first_htdf_problem) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;Problem: Design a function that pluralizes a given word.
;(Pluralize means to convert the word to its plural form.)
;For simplicity you may assume that just adding s is enough to pluralize a word.

;; String -> String

;; Produce the given string with "s" added to the end.

;(define (pluralize my_string) "")  ; stub

(check-expect (pluralize "cat") "cats")
(check-expect (pluralize "friend") "friends")

;(define (pluralize my_string) ; template
;  (... my_string)
;  )

;body
(define (pluralize my_string)
  (string-append my_string "s")
  )


