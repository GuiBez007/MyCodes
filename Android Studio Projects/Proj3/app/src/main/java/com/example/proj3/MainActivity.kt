package com.example.proj3

import android.os.Bundle
import android.view.View
import android.widget.EditText
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
    }

    fun calcularCombustivel(view : View) {
        val textNumber1 = findViewById<EditText>(R.id.textNumber1).text.toString()
        val textNumber2 = findViewById<EditText>(R.id.textNumber2).text.toString()

        if (validador(textNumber1, textNumber2))
            calcularMelhorPreco(textNumber1, textNumber2)
        else
            findViewById<TextView>(R.id.textView2).setText("Dado inválido ou faltante!")
    }

    fun validador(textNumber1: String, textNumber2: String): Boolean {
        var validado = true
        if (textNumber1 == null || textNumber1.equals(""))
            validado = false
        else if (textNumber2 == null || textNumber2.equals(""))
            validado = false
        return validado
    }

    fun calcularMelhorPreco(textNumber1: String, textNumber2: String) {
        val alcool = textNumber1.toDouble()
        val gasolina = textNumber2.toDouble()

        if (alcool / gasolina >= 0.7)
            findViewById<TextView>(R.id.textView2).setText("Melhor utilizar gasolina!")
        else
            findViewById<TextView>(R.id.textView2).setText("Melhor utilizar álcool!")
    }
    // apply plugin: 'kotlin-android-extensions'
}