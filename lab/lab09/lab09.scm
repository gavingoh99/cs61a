;; Scheme ;;

(define (over-or-under a b)
  (cond ((> a b) 1) ((< a b) -1) (else 0))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

(define (filter-lst fn lst)
  (if (null? lst)
      ()
      (if (fn (car lst))
          (cons (car lst) (filter-lst fn (cdr lst)))
          (filter-lst fn (cdr lst))))
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder n)
  (lambda (x) (+ x n))
)

;(define (make-adder n)
    ;(define (adder x)
      ;(+ x n))
  ;adder
;)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

;; Extra questions

(define lst
    ;(cons (cons 1 nil) (list 2 (cons 3 '(4)) 5))
    (list (list 1) 2 (list 3 4) 5)
)

(define (composed f g)
  (define (composite x)
      (f (g x)))
  composite
)

(define (remove item lst)
  (define (isitem? x) (not (= item x)))
  (filter-lst isitem? lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
    (if (null? s)
        ()
        (cons (car s)
              (no-repeats (filter-lst (lambda (a) (not (= a (car s)))) (cdr s)))))
)

(define (substitute s old new)
  (if (null? s)
      ()
      (if (eq? (car s) old)
          (cons new (substitute (cdr s) old new))
          (if (pair? (car s))
              (cons (substitute (car s) old new) (substitute (cdr s) old new))
              (cons (car s) (substitute (cdr s) old new)))))
)


(define (sub-all s olds news)
;base case is if reached the end of s or if there are no more words to be replaced, return s
  (if (or (null? s) (null? olds))
      s
      ;then we call sub-all recursively by calling substitute with the first old and first new element to form a processed s that is passed into sub-all 
      ;recursive calls to sub-all which again calls substitute with second old and second new to return a processed s... so on until s is null or old is null
      (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
)