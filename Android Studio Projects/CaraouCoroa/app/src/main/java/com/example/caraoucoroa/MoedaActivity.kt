package com.example.caraoucoroa

import android.os.Bundle
import android.util.Log
import android.widget.ImageButton
import android.widget.ImageView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MoedaActivity : AppCompatActivity() {
    var imgMoeda : ImageView? = null
    var imgBtnVoltar : ImageButton? = null
    var num : Int? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_moeda)

        mainConfig()
        mudarImagem()
        listeners()

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
    }

    private fun mainConfig() {
        imgMoeda = findViewById<ImageView>(R.id.imgMoeda)
        imgBtnVoltar = findViewById<ImageButton>(R.id.imgBtnVoltar)
        num = intent.extras?.getInt("sorteado")
    }

    private fun listeners() {
        imgBtnVoltar?.setOnClickListener() {
            finish()
        }
    }

    private fun mudarImagem() {
        if (num == 0)
            imgMoeda?.setImageResource(R.drawable.moeda_cara)
        else
            imgMoeda?.setImageResource(R.drawable.moeda_coroa)
    }
}